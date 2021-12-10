# export命令语法
* export [参数]
## 命令参数
    -f：指向函数。
    -n：删除变量的导出属性。
    -p：显示全部拥有导出属性的变量。
    -pf：显示全部拥有导出属性的函数。
    -nf：删除函数的导出属性。
## 配置网络代理
    export http_proxy=socks5://192.168.57.198:10808
    export https_proxy=socks5://192.168.57.198:10808
    export -p ##查看代理
    export -n http_proxy ##清除代理
