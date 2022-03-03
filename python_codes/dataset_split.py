"""
将数据集按80%train和20%val的比例分配。python dataset_split.py --dir /data/home/zgl/datasets/robot
文件结构
├── images #存放图片
├── labels
"""

import os
import glob
import shutil
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dir',
    type=str,
    default='None',
    help='data path ')
args, unparsed = parser.parse_known_args()

data_path = args.dir #数据根目录
print(data_path)

## 断言文件夹中必须包含classes.txt, voc.yaml, yolov5_model.yaml这三个文件夹
name_ = os.path.basename(data_path)
# print(name_)
# name_='robot'
classes_file = os.path.join(data_path, "classes.txt")
data_file = os.path.join(data_path, "voc_" + name_ + ".yaml")
model_file = os.path.join(data_path, "yolov5_model_" + name_ + ".yaml")
assert os.path.exists(classes_file), classes_file + " is not exist !"
assert os.path.exists(data_file), data_file + " is not exist !"
assert os.path.exists(model_file), model_file + " is not exist !"

## 将train,val中的图片移动到根目录，然后统一分配
for root, dirs, files in os.walk(os.path.join(data_path,"images")):
    for raw_name in files:
        raw_file = os.path.join(root, raw_name)
        move_file = os.path.join(data_path, raw_name)
        if raw_name.endswith(".jpg") or raw_name.endswith(".txt"):
            if not os.path.exists(move_file):
                shutil.move(raw_file, move_file)

for root, dirs, files in os.walk(os.path.join(data_path,"labels")):
    for raw_name in files:
        raw_file = os.path.join(root, raw_name)
        move_file = os.path.join(data_path, raw_name)
        if raw_name.endswith(".jpg") or raw_name.endswith(".txt"):
            if not os.path.exists(move_file):
                shutil.move(raw_file, move_file)

## 分配根目录下的文件到train和val文件夹
split_ratio = 0.8
label_list = glob.glob(os.path.join(data_path, "*.txt"))
train_labels = label_list[:int(split_ratio*len(label_list))]
val_labels = label_list[int(split_ratio*len(label_list)):]

count = 0
for type_ in ["train", "val"]:
    os.makedirs(os.path.join(data_path, "images", type_), exist_ok=True)
    os.makedirs(os.path.join(data_path, "labels", type_), exist_ok=True)

    if type_ == "train":
        labels = train_labels
    else:
        labels = val_labels
    
    for label_file in labels:
        label_name = os.path.basename(label_file)
        image_name = label_name[:-4] + ".jpg"
        image_file = label_file[:-4] + ".jpg"
        if os.path.exists(image_file):
            # print(image_file)
            # os.rename(image_file, os.path.join(data_path, "images", type_ ,image_name))
            # os.rename(label_file, os.path.join(data_path, "labels", type_ ,label_name))
            img = cv2.imread(image_file)
            cv2.imwrite(os.path.join(data_path, "images", type_ ,image_name),img)
            os.remove(image_file)
            os.rename(label_file, os.path.join(data_path, "labels", type_ ,label_name))
            count += 1
            if count % 100 == 0:
                print(count, "allocation already.")

## 将根目录下的多余的jpg文件移动到images目录下
for jpg_file in glob.glob(os.path.join(data_path,"*.jpg")):
    jpg_name = os.path.basename(jpg_file)
    move_file = os.path.join(data_path,"images/train", jpg_name)
    shutil.move(jpg_file, move_file)