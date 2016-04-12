#!/usr/bin/bash
set -xe
project_name='GrovePiUnit'
project_name_tar=$project_name.tar.gz
grove_host='192.168.14.19'
source ~/.bash_profile
ping -c 1 $grove_host
resp=$(ping -c 1 $grove_host | grep "1 received")
echo "======ping status========"
echo $resp
echo "========Removing exiting TAR========="
cd ../
if [ -f $project_name_tar ]; then
  rm $project_name_tar
fi
echo "========Zipping========"
tar -zcf $project_name_tar $project_name/
ls -l ~/PycharmProjects/$project_name_tar
chmod 777 $project_name_tar
echo "=====Uploading code to PI======="
scp ~/PycharmProjects/$project_name_tar pi@$grove_host:~/Documents/
echo "=====Removing old code from PI========"
ssh pi@$grove_host "rm -rf ~/Documents/$project_name"
echo "=====Unzipping PI TAR======="
#ssh pi@$grove_host "cd ~/Documents/; mkdir $project_name ;chmod +755 $project_name"
ssh pi@$grove_host "cd ~/Documents/; tar zxvf $project_name_tar -C ~/Documents/"
ssh pi@$grove_host  "ls -l ~/Documents/"
#ssh pi@$grove_host "cd ~/Documents/$project_name; python run.py"
ssh pi@$grove_host
