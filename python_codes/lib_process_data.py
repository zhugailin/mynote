import xml.etree.ElementTree as ET
import os
import shutil
import glob

def convert(size, box):
 
    x_center = (box[0] + box[1]) / 2.0
    y_center = (box[2] + box[3]) / 2.0
    x = x_center / size[0]
    y = y_center / size[1]
 
    w = (box[1] - box[0]) / size[0]
    h = (box[3] - box[2]) / size[1]
    
    return (x, y, w, h)

def voc2yolo(xml_file, classes):
    """
    voc格式xml_file转成yolo格式txt_file
    return:
        labels: xml_file包含的label数量，格式为， {"aqszc":2, ...}
        info: 字符串，yolo格式的标签信息，
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    info = ""
    labels = {}
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        
        if cls in labels:
            labels[cls] += 1
        else:
            labels[cls] = 1

        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
            float(xmlbox.find('ymax').text))
        # b=(xmin, xmax, ymin, ymax)
        # print(w, h, b)
        if w > 0 and h > 0 and all(x > 0 for x in b): # w, h, b必须都大于0
            bb = convert((w, h), b)
            info = info + str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n'
    
    return labels, info


def split_data(save_dir):
    """
    分配数据到文件夹
    """
    ## 将所有文件移动到save_dir根目录下，方便统一分配
    for root, dirs, files in os.walk(save_dir):
        for file_name in files:
            out_file = os.path.join(save_dir, file_name)
            in_file = os.path.join(root, file_name)
            if not os.path.exists(out_file):
                os.rename(in_file, out_file)
    
    ## 将save_dir目录下的jpg和txt统一分配
    label_list = glob.glob(os.path.join(save_dir, "*.txt"))
    train_labels = label_list[:int(0.9*len(label_list))]
    val_labels = label_list[int(0.9*len(label_list)):]

    type_ = "train"
    for txt_file in train_labels:
        img_dir = os.path.join(save_dir, "images", type_)
        os.makedirs(img_dir, exist_ok=True)
        txt_dir = os.path.join(save_dir, "labels", type_)
        os.makedirs(img_dir, exist_ok=True)
        img_file = txt_file[:-4] + ".jpg"
        if os.path.exists(img_file) and os.path.exists(txt_file):
            os.rename(txt_file, os.path.join(txt_dir, os.path.basename(txt_file)))
            os.rename(img_file, os.path.join(img_dir, os.path.basename(img_file)))
        img_file = txt_file[:-4] + ".JPG"
        if os.path.exists(img_file) and os.path.exists(txt_file):
            os.rename(txt_file, os.path.join(txt_dir, os.path.basename(txt_file)))
            os.rename(img_file, os.path.join(img_dir, os.path.basename(img_file)))

    type_ = "val"
    for txt_file in val_labels:
        img_dir = os.path.join(save_dir, "images", type_)
        os.makedirs(img_dir, exist_ok=True)
        txt_dir = os.path.join(save_dir, "labels", type_)
        os.makedirs(img_dir, exist_ok=True)
        img_file = txt_file[:-4] + ".jpg"
        if os.path.exists(img_file) and os.path.exists(txt_file):
            os.rename(txt_file, os.path.join(txt_dir, os.path.basename(txt_file)))
            os.rename(img_file, os.path.join(img_dir, os.path.basename(img_file)))
        img_file = txt_file[:-4] + ".JPG"
        if os.path.exists(img_file) and os.path.exists(txt_file):
            os.rename(txt_file, os.path.join(txt_dir, os.path.basename(txt_file)))
            os.rename(img_file, os.path.join(img_dir, os.path.basename(img_file)))
    