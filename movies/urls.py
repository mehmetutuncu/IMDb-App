from django.urls import path
from movies.resource.views import Top250MoviesView, MostPopularMoviesView
app_name = "movies"

urlpatterns = [
    path('top-250-movies', Top250MoviesView.as_view(), name='Top250Movies'),
    path('most-popular-movies', MostPopularMoviesView.as_view(), name='MostPopularMovies'),
]