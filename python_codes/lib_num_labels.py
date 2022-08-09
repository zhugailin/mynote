"""计算文件夹下标签和图片的数目
"""


import os
import glob
import json

all_dir = 'D:\\BaiduNetdiskDownload\\data'
# all_dir = "./data_xml"
xml_count_all = 0
jpg_count_all = 0
rate_all = {}

for root, dirs, files in os.walk(all_dir):

    for dir_ in dirs:
        jpg_list = glob.glob(os.path.join(root, dir_, "*.jpg")) + glob.glob(os.path.join(root, dir_, "*.JPG"))
        if len(jpg_list) > 0:
            print("jpg numbers in", os.path.join(root, dir_), "is", str(len(jpg_list)))
            jpg_count_all += len(jpg_list)

        xml_list = glob.glob(os.path.join(root, dir_, "*.xml"))
        if len(xml_list) > 0:
            try:
                print("xml numbers in", os.path.join(root, dir_), "is", str(len(xml_list)))
            except:
                continue
            xml_count_all += len(xml_list)

            rate = {}
            for xml_file in xml_list:
                for line in open(xml_file, "r", encoding='utf-8'):
                    if "<name>" in line:
                        label = line.split("name")[1][1:-2]
                        print(label)
                        if label in rate:
                            rate[label] += 1
                        else:
                            rate[label] = 1
                        
                        if label in rate_all:
                            rate_all[label] += 1
                        else:
                            rate_all[label] = 1
            print(rate)

print("xml文件总数是:", xml_count_all)
print("jpg文件总数是:", xml_count_all)
print("目标物总统计：", rate_all)

## 保存成json

json_str = json.dumps(dict(rate_all),ensure_ascii=False)
with open('./data_num.json', mode='w', encoding='utf-8') as json_file:
    json_file.write(json_str)

# f = open("./data_num.json", "w", encoding='utf-8')
# json.dumps(rate_all, ensure_ascii=False, indent=2, sort_keys=True)
# f.close()

