echo "installing the python....."
sudo apt-get install python
echo "pyhton has been installed"
echo "installing the pip for python"
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
python wingify_ecomm/manage.py runserver 
