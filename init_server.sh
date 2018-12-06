#/bin/sh

#install tool
apt-get update
apt-get install apache2
apt-get install mysql-server
/etc/init.d/mysql start

#download github
mkdir project
git clone  https://github.com/736094465/python.git ./project/
cd project/
git config --global user.email "736094465@qq.com"
git config --global user.name "736094465"
