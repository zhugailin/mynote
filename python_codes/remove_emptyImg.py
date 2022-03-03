"""
将数据集中没有标签的文本删除、图片移到其他地方
"""


import glob
import os 
import os.path 
import shutil 
import time,  datetime
txt_file = glob.glob('D:\datasets\\suspended2\obj_train_data/*.txt')
# print(aa)
for empty_txt in txt_file:
    pictureFileName=empty_txt.split('.')[0]
    if len(open(empty_txt,'r').readlines())==0:
        print(empty_txt)
        os.remove(empty_txt)                                        #移除没有空标签的文件
        shutil.copy(pictureFileName+".jpg", "D:\datasets\\suspended2/")    #把这些图片移出