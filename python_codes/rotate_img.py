import os 
import cv2
import glob
from sys import exc_info
from PIL import Image, ExifTags, ImageDraw, ImageFont


dir='E:\share\datasets\\robot\\unhelmet\obj_train_data//'

def get_exif_info(img_file, tag='Orientation'):
    """
    获取图片的exif信息。
    """
    item = None
    ## 用循环查找自己需要的信息的item。
    for it in ExifTags.TAGS.keys():
        if ExifTags.TAGS[it]==tag:
            item = it
            break 
    if item is None:
        return None

    img = Image.open(img_file)
    return img._getexif()[item]


def img_rotate_batch(dir):
    """
    将文件夹中带旋转信息的图片进行旋转。防止标注错误。
    """
    for root, dirs, files in os.walk(dir):
        
        for file_name in files:
            if not file_name.endswith((".jpg",".JPG",".png",".PNG",".bmp")):
                continue
            img_file = os.path.join(root, file_name)

            ## 删除无法用cv2.imread()读取的图片。
            data = cv2.imread(img_file)
            if data is None:
                os.remove(img_file)
                print(img_file, "remove already !")

            # try:
            img = Image.open(img_file)
            exif = img._getexif()
            if exif == None or 274 not in exif:
                img.close()
                continue
            if exif[274] == 3: ## 274是旋转信息的id
                angle = 180
            elif exif[274] == 6:
                angle = 270
            elif exif[274] == 8:
                angle = 90
            else:
                angle = 0
            if angle != 0:
                img=img.rotate(angle, expand=True)
                print(img_file,"rotated", angle, "already!")
                img.save(img_file)
            img.close()
            # except:
            #     continue

img_rotate_batch(dir)
    