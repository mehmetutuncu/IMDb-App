from django.urls import path
from tv_shows.resource.views import Top250TvShowsView, MostPopularTvShowsView

app_name = "tv-shows"

urlpatterns = [
    path('top-250-tv-shows', Top250TvShowsView.as_view(), name='Top250TvShows'),
    path('most-popular-tv-shows', MostPopularTvShowsView.as_view(),
         name='MostPopularTvShows'),
]
