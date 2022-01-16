from IMDB_APP.celery import app
from utils.service import IMDBService
from movies.models import Movie


@app.task()
def top_250_movies():
    Movie.objects.all().update(is_top_250=False, top_250_order=0)
    service = IMDBService()
    service.top_250_movies()


@app.task()
def most_popular_movies():
    Movie.objects.all().update(is_most_popular=False, most_popular_order=0)
    service = IMDBService()
    service.most_popular_movies()
