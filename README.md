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

##### server (Ubuntu 64bit, quad core, 4gb RAM, 30gb HDD)

###### Установка Python3

Втерминале по очерёдно введём команды

sudo su.
_______________
apt-get update.
_______________
apt-get upgrade
_______________
apt-get install python3.10
_______________
apt install python3-pip
_______________
python3 -m pip install --upgrade pip
_______________
установите пакеты требуемые для работы тестов
_______________
pip install selenium
_______________
pip install requests
_______________
pip install pytest
_______________
pip install beautifulsoup4
_______________
создайте папку под проекты
_______________
перейдите в неё
_______________
если у вас не установлен git используйте команду 
_______________
apt-get install git
_______________
затем выйдите из под root и клонируйте репозиторий
_______________
git clone https://github.com/imNa1s/serious_tests.git
_______________
после копирования репозитория перейдите в папку проекта и переименуйте conftest_win.py или conftets_headless.py в conftets.py
_______________
conftest_win.py - запускает тесты в полноэкранном режиме (для дебагинга)
_______________
conftest_headless.py - запускает тесты без графического интерфейса (для работы на сервере)

Установите распаковщик архивов
_______________
apt unzip
_______________
скачайте и установите chromedriver
_______________
wget https://chromedriver.storage.googleapis.com/{актуальная версия браузера}/chromedriver_linux64.zip
_______________
unzip chromedriver_linux64.zip
_______________
переходим в папку с chromedriver
_______________
перемещаем chromedriver
_______________
mv chromedriver /usr/bin
_______________
переходим в usr/bin
_______________
cd /usr/bin
_______________
chmod a+x chromedriver
_______________
установите Google Chrome соответствующей версии.

Для запуска тестов перейдите в home/{имя_пользователя}/serious_tests/tests
_______________
используйте команды вида pytest -v -m "admin" Test_login.py
_______________
где -m маркер соответсвующий нужному тесту
