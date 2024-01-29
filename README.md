# Test Work
Тест для компании FGUP GAMMA

Stack:
Python 3.10
Django==4.2.5
django-phonenumber-field==7.3.0
django-phonenumbers==1.0.1
phonenumbers==8.13.28
sqlparse==0.4.4
typing_extensions==4.9.0
tzdata==2023.4

## Repository Content
The reposytory contains 2 tasks:
1. Folder 'Task1' - code for colecting triplets from list of digits
    to run the code please enter commands below:  
```bash
cd task1
python main_clean.py
```
The folder also contains file 'main_with_comments.py'
In case you are interested in intermediate printouts and efficiensy of code 
please run command :  
```bash
python main_with_comments.py
```

2. Django project

Folder 'task_post'

to run Django project on test server please enter commands below:
```bash
cd task_post
pip install -r requirements.txt
python manage.py runserver
```
After you started test server, please open browser and enter as web address: 
```bash
http://127.0.0.1:8000
```
After that you will get access to working web page.


## FAQ

### Как запустить тесты
Тесты запускаем из директории src
```bash
pdm run python manage.py test
```
   
### Django Fixture download:
set of fixtures are already created for the project.
In case you will start project with clean database, please enter commands:
```bash
python manage.py makemigrations
python manage.py migrate
ruthon manage.py loaddata ./fixtures/001_all.json
```

### Django Fixture creation
In case you need to create fixture, please enter command:
```bash
python -Xutf8 manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude auth.group  --exclude admin.logentry --exclude sessions --indent 2 -o ./fixtures/009_all.json
```