sudo yum install libffi-dev git libi2c-dev i2c-tools minicom
sudo yum install python-devel.x86_64
wget https://bootstrap.pypa.io/get-pip.py -O - | python

cd ../
pip install virtualenv
virtualenv -p /usr/lib/python2.7 groveEnv
source groveEnv/bin/activate
tempdir=`mktemp -d`
cd $tempdir
wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.1.0.tar.gz
tar zxf RPi.GPIO-0.1.0.tar.gz
cd RPi.GPIO-0.1.0
sudo python setup.py install
cd -