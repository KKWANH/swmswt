#updateing & install virtual env
#- cluster mac
# python3	-m pip install --upgrade pip
# python3	-m pip install --user --upgrade pip
# python3	-m pip install --user virtualenv
#- local
python3	-m pip install --upgrade pip
python3	-m pip install --upgrade pip
python3	-m pip install virtualenv

#setting virtual env
python3	-m virtualenv ft_env
source	ft_env/bin/activate

#updating pip version
pip3 install --upgrade pip

#installing python libraries
pip3 install selenium