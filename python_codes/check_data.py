from asyncore import file_dispatcher
import os

save_dir = './data'

count = 0 
for root, dirs, files in os.walk(save_dir):
    for file_name in files:
        try:
            file_name.encode()
        except:
            count += 1
            os.rename(os.path.join(root, file_name), os.path.join(save_dir,file_name))
print("无法编码的数量为：",count)


# a= ['ding.jpg','\udcc6\dhfk.jpg']
# count = 0 
# for i in a:
#     print(type(i))
#     try:
#         i.encode()
#     except:
#         count += 1
#         print(count)
















# import os

# save_dir = './data/'

# count = 0 
# for root, dirs,files in os.walk(save_dir):
#     for file_name in files:
#         count += 1
#         new_file = save_dir + "error_" + str(int(count)).zfill(6) + file_name[-4:]
#         print(new_file)
#         os.rename(os.path.join(root, file_name), new_file)
# print("无法编码的数量为：",count)