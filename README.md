# TERmux

在Termux里安装Python

apt-get update

apt-get install python

apt-get install pip

apt-get install vim

termux-setup-storage
弹出读取手机存储照片权限，点击同意。termux会在/data/data/com.termux/files/home/目录中生成storage目录，里面有个shared目录其实就是/sdcard/的软连接
cd storage/shared
如果test.py文件放在/emulate/0/或者/sdcard/下面，这时要运行test.py就输入：
python /sdcard/test.py
