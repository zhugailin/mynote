import os
 
class BatchRename():
 
    def rename(self):
        path = "E:\\share\\datasets\data_yunnan\\云南招投标违章视频"
        filelist = os.listdir(path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.zip'):
                src = os.path.join(os.path.abspath(path), item)
                dst = os.path.join(os.path.abspath(path), ''+str(i)+'.avi')
                try:
                    os.rename(src, dst)
                    i += 1
                except:
                    continue
        print('total %d item to rename & converted %d avi'%(total_num, i))
 
if __name__=='__main__':
    demo = BatchRename()
    demo.rename()