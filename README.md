### IMDB Application developed with:
* Python
* Django 
* Celery & Redis
* PostgreSQL


### Installation:
```
1. docker-compose up -d 
2. pip install -r requirements.pip
3. python manage.py makemigrations && python manage.py migrate 
3. python manage.py runserver
4. celery -A IMDB_APP worker -l INFO
5. celery -A IMDB_APP beat -l INFO
```
example output: 
```
Watching for file changes with StatReloader
System check identified no issues (0 silenced).
January 16, 2022 - 14:31:37
Django version 3.2.11, using settings 'IMDB_APP.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Go to http://127.0.0.1:8000/ via browser.

### Screenshot: 
![screenshot](https://i.ibb.co/3CMSTmV/image.png)
