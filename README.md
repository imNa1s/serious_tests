# serious_tests
### This test suite is being developed for the Serious service. Contains a set of functional test scripts implemented in Python. Prepared for cyclical minor testing of the platform. 
#### The project is created with:
Python: 3.10
selenium: n4.1.0
pytest: 6.2.5
requests: 2.26.0
beautifulsoup4: 4.10.0

#### Setup
To run this project, install package to yours IDE or server

##### IDE (PyCharm for example)

~~

##### server (ubuntu 64bit, quad core, 4gb RAM, 30gb HDD)
установка python

sudo su

apt-get update
apt-get upgrade
apt-get install python3.10
apt install python3-pip
python3 -m pip install --upgrade pip
установите пакеты требуемые для работы тестов
pip install selenium
pip install requests
pip install pytest
pip install beautifulsoup4
создайте папку под проекты
перейдите в неё
если у вас не установлен git используйте команду 
apt-get install git
а затем выйдите из под root и клонируйте репозиторий
git clone https://github.com/imNa1s/serious_tests.git
после копирования репозитория перейдите в папку проекта и переименуйте conftest_win.py или conftets_headless.py в conftets.py
conftest_win.py - запускает тесты в полноэкранном режиме (для дебагинга)
conftest_headless.py - запускает тесты без графического интерфейса (для работы на сервере)

установите распаковщик архивов
apt unzip
скачайте и установите chromedriver
wget https://chromedriver.storage.googleapis.com/{актуальная версия браузера}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
переходим в папку с chromedriver
перемещаем его
mv chromedriver /usr/bin
переходим в usr/bin
cd /usr/bin
chmod a+x chromedriver
установите Google Chrome соответствующей версии

для запуска тестов перейдите в home/{имя_пользователя}/serious_tests/tests
используйте команды вида pytest -v -m "admin" Test_login.py
где -m маркер соответсвующий нужному тесту
