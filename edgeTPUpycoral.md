# coral
* 环境配置
 ~~ # None of this is needed on Coral boards
# This repo is needed for almost all packages below
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
# This repo is needed for only python3-coral-cloudiot and python3-coral-enviro
echo "deb https://packages.cloud.google.com/apt coral-cloud-stable main" | sudo tee /etc/apt/sources.list.d/coral-cloud.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update~~
  
* demo[]()
