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

## <div align="center">Docker</div>
<details close>
<summary>docker配置</summary>
安装docker
  
```bash
## 官方安装
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
## 国内安装
curl -sSL https://get.daocloud.io/docker | sh
```
</details>

<details close>
<summary>加入docker组</summary>
使用docker时不用sudo
  
```bash
## 添加docker组
sudo groupadd docker
## 用户添加到docker组
sudo gpasswd -a ${USER} docker
## 重启docker
sudo service docker restart
## 退出shell重新进入就完成了。
```
</details>

<details close>
<summary>docker操作</summary>
配置镜像
  
```bash
## 下载镜像
docker pull ultralytics/yolov5:v5.0
## 镜像提交更改
docker commit -a "yh_test" -m "build detectron2 develop" bc94bd5dc434  yh/dnn:ub18-cuda11.1-conda-trt7.2
## 打包镜像
docker save -o yh_dnn.tar yh/dnn:ub18-cuda11.1-conda-trt7.2
本地载入镜像
docker load --input yh_dnn.tar
```
常用命令

```bash
docker images # 查看所有镜像
docker run # 运行docker
docker ps # 查看正在运行的docker
docker attach # 加入运行中的镜像
docker stop # 停止正在运行的镜像
docker start # 开始运行镜像
Ctrl+P+Q # 退出容器
## 开机自启动docker
docker update --restart=always yh_inspection
```
docker run 命令

```bash
docker run 
    -it \  # 必须
    --gpus '"device=0,1"' \ # 使用gpu
    --name "yh_test" \ # 命名
    -p 8042:22 \ # 端口映射
    --ipc=host \
    -v /home/yh/image:/home/yh/image \ # 文件夹映射
    -e LANG=C.UTF-8 -e LC_ALL=C.UTF-8 \ # 改编码格式
    yh/dnn:ub18-cuda11.1-conda-trt7.2 /bin/bash
```
docker内部配置ssh映射

```bash
mkdir /var/run/sshd
echo 'root:Yuan930216' | chpasswd
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
echo "export VISIBLE=now" >> /etc/profile
service ssh restart
```
</details>

## <div align="center">NVIDIA</div>
<details close>
<summary>nvidia配置</summary>
安装nvidia驱动
  
```bash
## 查看最新驱动
ubuntu-drivers devices
## 安装驱动
sudo apt-get install nvidia-driver-470  ## 可选择最新版本
## 重启生效
```
安装docker需要的--gpu插件
  
``` bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```
</details>

## <div align="center">GIT</div>
<details close>
<summary>git命令</summary>
环境配置
  
```bash
## 生成密钥
ssh-keygen -t rsa -C "yuanhui@ut.cn"
```
git常用命令
  
```bash
git commit -m "" # 提交更新 
## 新建分支并 进入分支
{git branch bugFix; git checkout bagFix; git commit} = {git checkout -b bugFix}
git merge bugFix # 合并分支
git rebase main # 顺序合并分支
## 移动HEAD
git checkout HEAD^ ;  git checkout HEAD~4 ; git branch -f main HEAD~3
## 从远程仓库提取数据
git fetch # 将log提取下来，本地库代码不变
## 直接更新本地库
git pull = {git fetch; git merge o/main)
## 远程库添加伪提交
git fakeTeamwork foo 3
```
git 实练命令
  
```bash
git tag \ # 查看tag
    --contains 11528ce083dc9ff83ee3a8f908  # 查看包含此提交的tag
git stash # 暂存
```
</details>

## <div align="center">其他命令</div>
screen的使用
  
```bash
screen
    -ls # 查看存在的screen
    -dms  yh_test # 创建screen
    -r yh_test # 加入screen
    exit # 退出并删除screen
```
rsync,不同服务器之间目录同步

```bash
rsync -r -K --delete /dataset/uploading_data/ yuanhui@172.26.12.14:/dataset/uploading_data/
```
vim常用命令

```bash
nyy/P # 复制粘贴
## 搜索关键词
/user  # 表示搜索user
## 替换关键字
:n,$s/vivian/sky/g # 替换第 n 行开始到最后一行中每一行所有 vivian 为 sky
```
查看cpu

```bash
## 查看逻辑核数量
cat /proc/cpuinfo| grep "processor"| wc -l
## 查看物理核数量
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
```

bytes, str, int, hex之间的转换: https://blog.csdn.net/xuzhexing/article/details/90766651


