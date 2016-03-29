echo "installing the python....."
sudo apt-get install python
echo "pyhton has been installed"
echo "installing the pip for python"

sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev

sudo easy_install greenlet

sudo easy_install gevent
sudo apt-get install python-pip
echo "done."
echo "installing the virtualenv for python"
sudo apt-get install virtualenv
echo "done."

echo "activating the virtul environment"
source env/bin/activate
echo "virtual environment has been activated"

echo "installing the dependencies of django"
pip install -r requirements.txt

echo "running command django-admin  makemigrations app.."

python wingify_ecomm/manage.py makemigrations app
python wingify_ecomm/manage.py migrate
python wingify_ecomm/manage.py loaddata app wingify_ecomm/app/db.json
python wingify_ecomm/manage.py runserver 
