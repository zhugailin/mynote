
import cv2
import argparse
import os

from sympy import stieltjes
def parse_args():
 
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Process pic')
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    #default为间隔多少帧截取一张图片
    parser.add_argument('--skip_frame', dest='skip_frame', help='skip number of video', default=10, type=int) #此处可更改提取帧的间隔
    args = parser.parse_args([
    '--input','E:\\share\\datasets\\tz\\tz_00017.avi',
    '--output','E:\\share\\datasets\\tz\\images'
    ])   #此处添加路径，input为输入视频的路径 ，output为输出存放图片的路径
    return args
    
def process_video(i_video, o_video, num):
    cap = cv2.VideoCapture(i_video) 
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    flie_name = 'tz_' + i_video[-9:-4] +'_'
    expand_name = '.jpg'
    if not cap.isOpened():
        print("Please check the path.")
    cnt = 0
    count = 0

    while 1:
        ret, frame = cap.read()
        if not ret:
            break
        # frame = cv2.resize(frame,(1280,720))   # 在尺寸可以修改图片尺寸
        cnt += 1
        if cnt % num == 0:
            count += 1
            print(os.path.join(o_video, flie_name + str(count).zfill(5) + expand_name))
            cv2.imwrite(os.path.join(o_video, flie_name + str(count).zfill(5) + expand_name), frame)
            
if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    print('Called with args:',args)
    process_video(args.input, args.output, args.skip_frame)
