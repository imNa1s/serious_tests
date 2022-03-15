# serious_tests
### This test suite is being developed for the Serious service. Contains a set of functional test scripts implemented in Python. Prepared for cyclical minor testing of the platform. 
#### The project is created with:

1. Python: 3.10
2. selenium: n4.1.0
3. pytest: 6.2.5
4. requests: 2.26.0
5. beautifulsoup4: 4.10.0
6. telebot 0.0.4

#### Setup
To run this project, install Python and package to yours IDE or server

##### IDE (PyCharm for example)

~~

##### Server (Ubuntu 64bit, quad core, 4gb RAM, 30gb HDD)

##### Установка Python3

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
12. pip install telebot
13. pip install pyTelegramBotApi

##### Установка Git и копирование репозитория.
Создайте папку под проекты и перейдите в неё.  
Если у вас не установлен git используйте команду:  
- apt-get install git. 
Затем выйдите из под root при помощи команды exit.  
Клонируйте репозиторий:  
- git clone https://github.com/imNa1s/serious_tests.git  
Важно!  
После копирования репозитория перейдите в папку проекта и переименуйте conftest_win.py, conftets_headless.py, или conftets_selenoid.py в conftets.py  
conftest_win.py - запускает тесты в полноэкранном режиме (для работы в Windows системах).  
conftest_headless.py - запускает тесты без графического интерфейса (для работы в системе Ubuntu).  
conftets_selenoid.py - запускает тесты в специальном контейнере (требуется установить дополнительное ПО)

##### Установка Chrome и chromedriver.
Установите распаковщик архивов (если не установлен).
- apt install unzip.
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


#### Setup Bot

Для запуска бота, откройте консоль, перейдите в папку с проектом, и выполните команду:  
- python serious_win_bot.py - для Windows систем.
- python serious_unix_bot.py - для Unix систем.

#### Setup Selenoid

##### Setup Docker for Selenoid

Если вы решили установить Selenoid уже после того как некоторое время пользовались тест сьютом обновите базу пакетов:  
- sudo apt update  

Для корректной работы требуется установить дополнительные пакеты:  
- sudo apt install apt-transport-https ca-certificates curl software-properties-common  

Добавляем ключ GPG официального репозитория Docker:  
- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add  

Подключаем репозиторий Docker:  
- sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"  

После добавления нового репозитория обязательно обновим базу пакетов, иначе при выполнении команды установки система не будет знать что этот пакет доступен:  
- sudo apt update  

Установим Docker:  
- sudo apt install docker-ce  

Для проверки активен ли докер используйте команду:  
- sudo systemctl status docker  

##### Setup Selenoid for Linux

Скачайте бинарник для быстрой установки Selenoid'а с официальной страницы релизов:  
- https://github.com/aerokube/cm/releases/tag/1.8.1  

Переименуйте его в "cm" для более удобного использования  

Выдайте права на выполнение:  
- chmod +x cm  

Запустите установку при помощи команды:  
- ./cm selenoid start --vnс  

Опционально можете установить Selenoid-UI командой:  
- ./cm selenoid-ui start  

##### Setup Selenoid for Windows

Скачайте установочник с официальной страницы релизов и запустите его.  
- https://github.com/aerokube/cm/releases/tag/1.8.1   
