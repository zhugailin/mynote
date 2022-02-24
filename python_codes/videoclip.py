## 读取视频，并逐帧切分成图片

import cv2 as cv
import os
os.chdir('/data/home/zgl/Github/python-opencv/')
cap =cv.VideoCapture("./video1.avi")
isOpened = cap.isOpened()  ##判断视频是否打开
print(isOpened)
fps = cap.get(cv.CAP_PROP_FPS)  ##获取帧率
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))   ###获取宽度
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))   ###获取高度
print(fps,width,height)
i=0
while isOpened :
    if i ==300:   ###只保存前300张
        break
    else:
        i= i+1
    (flag,frame)=cap.read()
    fileName = "image"+str(i)+".jpg"
    print(fileName)
    if flag == True :
        cv.imwrite("./images/"+str(i)+".jpg",frame,[cv.IMWRITE_JPEG_CHROMA_QUALITY,100])  ##命名 图片 图片质量
print("end!")
