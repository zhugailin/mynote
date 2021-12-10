# linux终端配置网络代理
```
export http_proxy=socks5://192.168.57.198:10808
export https_proxy=socks5://192.168.57.198:10808
export -p                   ##查看代理
export -n http_proxy        ##清除代理
```
    
    export [参数]
        -f：指向函数。
        -n：删除变量的导出属性。
        -p：显示全部拥有导出属性的变量。
        -pf：显示全部拥有导出属性的函数。
        -nf：删除函数的导出属性。
        
## <div align="center">配置环境</div>
<details close>
<summary>conda</summary>
搭建miniconda环境
  
```bash
sh Miniconda3-latest-Linux-x86_64.sh  
conda env export >  environment.yml
conda env create -f /home/yh/miniconda3/envs/environment.yml
pip install -r /home/yh/miniconda3/envs/request.txt
```
  
设置通道
  
```bash
conda config --remove-key channels
conda config --set show_channel_urls yes 
conda config --get channels
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ ## pytorch
```

设置代理
 
```bash
conda config --set proxy_servers.http http://192.168.57.61:10809
conda config --set proxy_servers.https https://192.168.57.61:10809
```
</details>

<details close>
<summary>cuda</summary>
搭建cuda安装环境
  
```bash
apt-get update
# vim;  gcc; g++; make; libxml2; libgl1-mesa-glx
``` 
非root用户安装：https://zhuanlan.zhihu.com/p/198161777 ;  root用户安装：https://zhuanlan.zhihu.com/p/72298520

安装例子
 
```bash
tar -zxvf cudnn-11.2-linux-x64-v8.1.1.33.tgz
cp cuda/include/cudnn.h /usr/local/cuda-11.1/include/ 
cp cuda/lib64/libcudnn* /usr/local/cuda-11.1/lib64/ 
chmod a+r /usr/local/cuda-11.1/include/cudnn.h 
chmod a+r /usr/local/cuda-11.1/lib64/libcudnn*
export CUDA_HOME=/usr/local/cuda-11.1
export PATH=/usr/local/cuda-11.1/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-11.1/lib64
nvcc -V
``` 
</details>

<details close>
<summary>TensorRT</summary>
安装tensorrt

```bash
tar xzvf TensorRT-7.2.3.4.Ubuntu-18.04.x86_64-gnu.cuda-11.1.cudnn8.1.tar.gz
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/TensorRT-7.2.3.4/lib
cp -r ./lib/* /usr/lib
cp -r ./include/* /usr/include
cd python
pip install tensorrt-5.0.2.6-py2.py3-none-any.whl
cd ../uff
pip install uff-0.5.5-py2.py3-none-any.whl
cd ../graphsurgeon
pip install graphsurgeon-0.3.2-py2.py3-none-any.whl
```  
</details>

<details close>
<summary>detectron2</summary>
安装detectron2

```bash
git clone https://github.com/facebookresearch/detectron2.git
## 1. 用pip安装
python -m pip install -e detectron2
## 2. 用build安装
cd detectron2
python setup.py build develop
```  
</details>

## <div align="center">杂烩</div>

bytes, str, int, hex之间的转换: https://blog.csdn.net/xuzhexing/article/details/90766651
