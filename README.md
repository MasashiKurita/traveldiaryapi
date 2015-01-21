traveldiaryapi
==============

## Requirement
    bash$ mysql --version
    mysql Ver 14.14 Distrib 5.5.40
    bash$ python -V
    Python 3.4.2
    bash$ pip freeze -l  
    Django==1.7.3  
    Markdown==2.5.2  
    djangorestframework==2.4.4  
    mysql-connector-python==2.0.2  


## Install & Run

### Create Database

    bash$ git clone https://github.com/MasashiKurita/traveldiaryapi.git
    bash$ cd traveldiaryapi
    bash$ mysql -u root -p
    Enter password:
    mysql> source create_database.sql
    
### Create Tables

    bash$ python manage.py makemigration
    bash$ python manage.py migrate

### Run

    bash$ python manage.py runserver