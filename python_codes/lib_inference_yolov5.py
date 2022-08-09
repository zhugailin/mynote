import cv2
import torch
import sys
import time
import os
import glob

sys.path.append('../yolov5') ## ultralytics/yolov5 存放的路径
from utils.datasets import letterbox
from utils.general import non_max_suppression, scale_coords
from models.common import DetectMultiBackend
import numpy as np
from utils.torch_utils import select_device
from models.experimental import attempt_download, attempt_load  # scoped to avoid circular import

device = select_device("0,1")  ## 选择gpu: 'cpu' or '0' or '0,1,2,3'

def load_yolov5_model(model_file):
    """
    # load yolov5 FP32 model
    """
    # yolov5_weights = DetectMultiBackend(model_file, device=device) #, dnn=False, data='data/coco128.yaml', fp16=False
    yolov5_weights = attempt_load(model_file , map_location=device) # 加载模型
    return yolov5_weights

def inference_yolov5(model_yolov5, img, resize=640, conf_thres=0.4, iou_thres=0.2):
    """
    使用yolov5对图片做推理，返回bbox信息。
    args:
        model_yolov5: 加载后的yolov5模型，使用load_yolov5_model(model_file)加载
        img_file: 需要预测的图片
    return:
        bbox_cfg: 预测的bbox信息，json文件格式为格式为[{"label": "", "coor": [x0, y0, x1, y1], "score": float}, {}, ..]
    """
    
    # img = cv2.imread(img_file)
    img_raw = img.copy()  #由于需要resize，先拷贝一份备用。

    ## 将numpy转成yolov5格式input data.
    img = letterbox(img, new_shape=resize)[0] # resize图片
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3 x 640 x 640
    img = torch.from_numpy(img.copy()).to(device) # numpy转tenso
    img = img.float()
    img /= 255  # 0 - 255 to 0.0 - 1.0
    img = img.unsqueeze(0) # 添加一维
    # if len(img.shape) == 3:
    #     img = img[None]  # expand for batch dim

    ## 使用yolov5预测
    pred = model_yolov5(img, augment=False, visualize=False)[0] # Inference

    ## 使用NMS挑选预测结果
    pred_max = non_max_suppression(pred, conf_thres, iou_thres)[0] # Apply NMS
    pred_max = scale_coords(img.shape[2:], pred_max, img_raw.shape) #bbox映射为resize之前的大小

    ## 生成bbox_cfg 的json格式，有助于人看[{"label": "", "coor": [x0, y0, x1, y1]}, {}, ..]
    labels = model_yolov5.module.names if hasattr(model_yolov5, 'module') else model_yolov5.names
    bbox_cfg = []
    for res in pred_max.cpu().numpy():
        bbox = {"label": labels[int(res[-1])], "coor": (res[:4]).astype(int).tolist(), "score": res[4]}
        bbox_cfg.append(bbox)

    # lib_image_ops.draw_bboxs(img_file, bbox_cfg, is_write=True)

    return bbox_cfg

def inference_batch(weights, source, save_dir, conf_thres=0.4, iou_thres=0.2):
    """
    使用yolov5模型推理图片，并保存成特殊格式。
    args:
        weights: yolov5模型文件，.pt结尾。
        soutce: 图片路径或者含有图片的文件夹。
        save_dir: 保存结果的文件夹。
    """
    ## 判断source是文件还是文件夹
    if os.path.isfile(source):
        img_list = [source]
    elif os.path.isdir(source):
        img_list = glob.glob(os.path.join(source,"*.jpg"))
    else:
        print(source, "not exists!")
        return 0
    ## 加载模型
    yolov5_weights = load_yolov5_model(weights)

    ## 创建文件夹
    os.makedirs(save_dir, exist_ok=True)
    label_dir = os.path.join(save_dir, "label")
    result_dir = os.path.join(save_dir, "result")
    os.makedirs(label_dir, exist_ok=True)
    os.makedirs(result_dir, exist_ok=True)

    ## 批处理
    for img_file in img_list:
        img = cv2.imread(img_file)
        # [{"label": "", "coor": [x0, y0, x1, y1], "score": float}, {}, ..]
        bbox_cfg = inference_yolov5(yolov5_weights, img, resize=640, conf_thres=conf_thres, iou_thres=iou_thres) #推理
        print("--------------------------------")
        print(img_file)
        print(bbox_cfg)
        ## 保存推理结果
        res_file = os.path.join(result_dir, os.path.basename(img_file)) 
        label_file = os.path.join(label_dir, os.path.basename(img_file)[:-4]+".txt")
        s = "ID,PATH,TYPE,SCORE,XMIN,YMIN,XMAX,YMAX\n"  
        count = 0
        for bbox in bbox_cfg:
            count += 1
            label = bbox["label"]
            score = bbox["score"]
            c = bbox["coor"]

            ## 将结果画在图上
            cv2.rectangle(img, (int(c[0]), int(c[1])),(int(c[2]), int(c[3])), (255,0,255), thickness=2)
            cv2.putText(img, label+": "+str(score), (int(c[0]), int(c[1])-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), thickness=2)

            ## 输出结果
            result = [str(count),os.path.basename(img_file),label,str(score),str(c[0]),str(c[1]),str(c[2]),str(c[3])]
            s = s + ",".join(result) + "\n"
        
        f = open(label_file, "w", encoding='utf-8')
        f.write(s)
        f.close()
        cv2.imwrite(res_file, img)


if __name__ == '__main__':
    weights = '/data/home/zgl/yolov5/runs/train/class_7_focal_200/weights/best.pt'
    source = "/home/yh/image/python_codes/test/test"
    save_dir = "./result"
    inference_batch(weights, source, save_dir, conf_thres=0.4, iou_thres=0.2)
