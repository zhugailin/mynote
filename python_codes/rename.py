  # -*- coding: UTF-8 -*-

# 试用范围：图片以.jpg结尾 文档以.txt结尾 图片与文档的名字相同
# 作用：可用于同时将图片与文档按顺序重命名

from operator import ne
import os
# path = 'D:\\datasets\测试文件\\测试文件\\'
path = 'E:\\share\\datasets\\dxg\\dxg2\\'
# 获取该目录下所有文件，存入列表中
files= os.listdir(path)
n = 1
new_name = 'dxg2'
for allnamejpg in files:
    n += 1
    # if(allnamejpg[-4:])=='.JPG' or (allnamejpg[-4:])=='.jpg' and allnamejpg[0:3]!='img': 
    # if ((allnamejpg[-4:])=='.JPG' or (allnamejpg[-4:])=='.png' ): #判断是jpg/JPG/png结尾的图片
    if (allnamejpg[-4:]) in (".jpg",".JPG",".png",".PNG",".bmp","jpeg"):
        length=len(allnamejpg)
        name = allnamejpg[:-4] # #截取从头开始到倒数第四个字符之前
        oldnamejpg=path+allnamejpg
        renamejpg = path + new_name + "_" + str(int(n)).zfill(5)+'.jpg'  #0填充xx_0000001.jpg
        os.renames(oldnamejpg, renamejpg)
        print (oldnamejpg+'======>'+renamejpg)

        for allnametxt in files:
            # if (allnametxt==name+'.txt') and allnametxt[0:2]!='gt':
            if allnametxt==name+'.txt':
                oldnametxt = path + allnametxt
                renametxt = path + new_name + "_" + str(int(n)).zfill(5) + '.txt'
                os.renames(oldnametxt, renametxt)
                print (oldnametxt + '======>'+renametxt)
                print (n)
        
