# serious_tests
### This test suite is being developed for the Serious service. Contains a set of functional test scripts implemented in Python. Prepared for cyclical minor testing of the platform. 
#### The project is created with:

1. Python: 3.10
2. selenium: n4.1.0
3. pytest: 6.2.5
4. requests: 2.26.0
5. beautifulsoup4: 4.10.0

#### Setup
To run this project, install Python and package to yours IDE or server

##### IDE (PyCharm for example)

~~

##### Server (Ubuntu 64bit, quad core, 4gb RAM, 30gb HDD)

###### Установка Python3

В терминале по очерёдно введём команды:
1. sudo su.
2. apt-get update.
3. apt-get upgrade
4. apt-get install python3.10
5. apt install python3-pip
6. python3 -m pip install --upgrade pip
7. установите пакеты требуемые для работы тестов
8. pip install selenium
9. pip install requests
10. pip install pytest
11. pip install beautifulsoup4

###### Установка Git и копирование репозитория.
Создайте папку под проекты и перейдите в неё.
Если у вас не установлен git используйте команду:
apt-get install git.
Затем выйдите из под root при помощи команды exit.
Клонируйте репозиторий:
git clone https://github.com/imNa1s/serious_tests.git
Важно!
После копирования репозитория перейдите в папку проекта и переименуйте conftest_win.py или conftets_headless.py в conftets.py.
conftest_win.py - запускает тесты в полноэкранном режиме (для дебагинга).
conftest_headless.py - запускает тесты без графического интерфейса (для работы на сервере).

###### Установка Chrome и chromedriver.
Установите распаковщик архивов (если не установлен).
- apt unzip.
Скачайте и установите chromedriver при помощи команд:
- wget https://chromedriver.storage.googleapis.com/{актуальная версия браузера}/chromedriver_linux64.zip
- unzip chromedriver_linux64.zip

Переходим в папку с chromedriver:
- cd {полный путь к папке}
Перемещаем chromedriver:
- mv chromedriver /usr/bin
Переходим в usr/bin:
- cd /usr/bin
Делаем cromedriver исполняемым:
- chmod a+x chromedriver


Установите Google Chrome соответствующей версии.
Для запуска тестов перейдите в home/{имя_пользователя}/serious_tests/tests.
Для запуска тестов используйте команды вида pytest -v -m "admin" Test_login.py.
Где после -m указывается маркер соответсвующий нужному тесту список маркеров находится в pytest.ini
