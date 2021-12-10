# coral
* 环境配置
  ```This repo is needed for almost all packages below
  echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
  This repo is needed for only python3-coral-cloudiot and python3-coral-enviro
  echo "deb https://packages.cloud.google.com/apt coral-cloud-stable main" | sudo tee /etc/apt/sources.list.d/coral-cloud.list

  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

  sudo apt-get update```

[demo](https://packages.cloud.google.com/)

# Edgetpu运行模型
 * 启动docker 
  docker run -it \
      --gpus all \
      --name="zgl_test_yolov5" -v /data/home/zgl/yh_image:/data/home/zgl/yh_image \
      -v /data/home/zgl/datasets/:/data/home/zgl/datasets/  \
      -v /data/home/zgl/:/data/home/zgl/ \
      zldrobit/yolov5:v4.0-tf2.4.1 bash
      
```
cd /data/home/zgl/yolov5_edgetpu/yolov5

python export.py --weight yolov5l.pt --include tflite –int8 –imgz 224 224  ##输出默认的640在执行edgetpu_compiler yolov5l-int8.tflite编译时会报错

edgetpu_compiler yolov5l-int8.tflite (编译问题可以参考链接：https://coral.ai/docs/edgetpu/compiler/#compiler-and-runtime-versions  

cd /coral/flask_triton/pycoral/flask_edgetpu

python detect_demo.py
 ```

