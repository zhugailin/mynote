import os
import collections #统计模块

in_path = r"E:\share\\datasets\\data_yunnan\\images\\cut"

def read_txt(in_path):
    classNum = []
    # file_list = os.listdir(in_path)  # 读取文件列表
    for filepath, dirnames, filenames in os.walk(in_path):
        for lists in filenames:
            temp1 = lists.split('.')[1]
            if temp1 == "txt":
                txt_path = os.path.join(filepath, lists)
                for line in open(txt_path, "r"):  # 设置文件对象并读取每一行文件
                    class_id = line.split(' ')[0]
                    classNum.append(class_id)  # 将每一行文件加入到list中
            else:
                continue
        num = collections.Counter(classNum)
        print(num)

read_txt(in_path)
