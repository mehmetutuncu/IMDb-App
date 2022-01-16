import requests
from movies.models import Movie


class IMDBClient():

    @staticmethod
    def _get(**kwargs):
        response = requests.get(**kwargs)
        response.raise_for_status()
        return response

    def top_250_movies(self):
        url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
        response = self._get(url=url)
        return response

    def most_popular_movies(self):
        url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
        response = self._get(url=url)
        return response

    def top_250_tv_shows(self):
        url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
        response = self._get(url=url)
        return response

    def most_popular_tv_shows(self):
        url = 'https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv'
        response = self._get(url=url)
        return response
