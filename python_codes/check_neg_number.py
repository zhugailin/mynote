from distutils import text_file
import os
import glob
from subprocess import _TXT

num = 0 
text_file = "D:\\BaiduNetdiskDownload\\sh_data"
for line in open(txt_file, "r", encoding="utf-8"):
    ls = line.strip().split(" ")
    for l in ls:
        if float(l) < 0:
            conut += 1
