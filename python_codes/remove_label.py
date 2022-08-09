"""
切分标签内容每行,然后对第一列的标签进行替换和计数
"""

from itertools import count
import os, glob

if __name__ == '__main__':
    txt_list = glob.glob("E:\share\\datasets\\17类缺陷中的ywzt_yfyc\\labels/*.txt")

    num = 0
    for txt_item in txt_list:
        with open(txt_item) as f:
            lines = f.readlines()
        with open(txt_item, 'w') as f:
            for line in lines:
                line_split = line.strip().split()

                
                if line_split[0] == '*':
                    del line_split[:]

                else:
                    f.write(
                        line_split[0] + ' ' +
                        line_split[1] + " " +
                        line_split[2] + " " +
                        line_split[3] + " " +
                        line_split[4]+'\n')
        
        pass
    print(num)
    print("over") 


