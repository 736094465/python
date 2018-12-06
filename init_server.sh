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
