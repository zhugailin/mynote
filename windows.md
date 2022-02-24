# Windows 用户CMD常用命令总结
## tips
- **help** 命令 ：查看帮助
- **Tab**键，自动补全

## 关机、重启、注销、休眠、定时
    关机：shutdown /s
    重启：shutdown /r
    注销：shutdown /l
    休眠：shutdown /h /f
    取消关机：shutdown /a
    定时关机：shutdown /s /t 3600（3600 秒后关机）

## 目录操作
- 切换磁盘：d:（进入 d 盘）
- 切换磁盘和目录：cd /d d:/test（进入 d 盘 test 文件夹）
- 进入文件夹：cd \test1\test2（进入 test2 文件夹）
- 返回根目录：cd \
- 回到上级目录：cd ..
- 新建文件夹：md test

## 网络操作
    延迟和丢包率：ping ip/域名
    Ping 测试 5 次：ping ip/域名 -n 5
    清除本地 DNS 缓存：ipconfig /flushdns
    路由追踪：tracert ip/域名

## 进程/服务操作
- 进程管理：

    - 显示当前正在运行的进程：tasklist
    - 运行程序或命令：start 程序名
    - 结束进程，按名称：taskkill /im notepad.exe（关闭记事本）
    - 结束进程，按 PID：taskkill /pid 1234（关闭 PID 为 1234 的进程）
- 服务管理：

    - 显示当前正在运行的服务：**net start**
    - 启动指定服务：net start 服务名
    - 停止指定服务：net stop 服务名
