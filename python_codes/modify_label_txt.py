"""
切分标签内容每行,然后对第一列的标签进行替换和计数
"""

from itertools import count
import os, glob

if __name__ == '__main__':
    txt_list = glob.glob("E:\share\\datasets\\17类缺陷中的ywzt_yfyc\\labels/*.txt")
    # list = ["0","1","11",'12',"13","15","17",'24',"25"]  #标签类目数
    num = 0
    for txt_item in txt_list:
        with open(txt_item) as f:
            lines = f.readlines()
        with open(txt_item, 'w') as f:
            for line in lines:
                line_split = line.strip().split()

                # if line_split[0] not in ["0","1"]: #1.检查是不是都在标签里，就删除掉
                #     num += 1
                #     print(txt_item)

                # if line_split[0] not in list: #2.检查是不是都在标签里，如果不在找出对应的
                # if line_split[0] == '0':      #如果不在先替换掉
                #     num += 1
                #     print(txt_item)

                # 替换对应标签
                if line_split[0] == '6':#
                    line_split[0] = '2'
                elif line_split[0] == '15':#
                    line_split[0] = '1'
                    num += 1
                    print(txt_item)

                f.write(
                    line_split[0] + ' ' +
                    line_split[1] + " " +
                    line_split[2] + " " +
                    line_split[3] + " " +
                    line_split[4]+'\n')
        
        pass
    print(num)
    print("over") 


