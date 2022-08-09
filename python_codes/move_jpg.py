# -*- coding: UTF-8 -*- 
# !/usr/bin/env python
import os
import shutil 
import sys
import re
from PIL import Image

"""
1.根据图片名匹配处相应的txt文件并将txt移动到指定文件夹
"""

# sys.path.append('E:/share/datasets')

# import numpy as np
# data = []
# list_dirs = 'E:\share\\datasets\\zhenhai\images\\'  #path of images
# for root, dirs, files in os.walk(list_dirs):
#     for f in files:
#         if os.path.splitext(f)[-1] == ".jpg" or os.path.splitext(f)[-1] == ".JPG":   #将jpg/JPG文件名放入列表
#             data.append(f)

# for a in data:
#     print(a)
#     try:
#         shutil.move('E:\share\\datasets\\zhenhai/labels\{}.txt'.format(a[:-4]),'E:\share\\datasets\\zhenhai/labels_modify\\{}.txt'.format(a[:-4]))    
#     except FileNotFoundError:
#         print(f"Sorry,the file {a[:-4]}.txt does not exist.")



"""
2.根据txt文件名匹配出相应图片并将图片移动到指定文件夹
"""

sys.path.append('E:\share/datasets')

import numpy as np
data = []
list_dirs = 'E:\share\\datasets\\tz\\images'  #path of images
for root, dirs, files in os.walk(list_dirs):
    for f in files:
        if os.path.splitext(f)[-1] == ".txt" :   #
            data.append(f)

for a in data:
    print(a)
    try:
        shutil.move('E:\share\\datasets\\tz\\images\\{}.jpg'.format(a[:-4]),'E:\share\\datasets\\tz\\images\\new_images\\{}.jpg'.format(a[:-4]))
    except FileNotFoundError:
        print(f"Sorry,the file {a[:-4]}.jpg does not exist.") #