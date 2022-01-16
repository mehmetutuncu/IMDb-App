from utils.client import IMDBClient
from bs4 import BeautifulSoup
from movies.models import Movie
from tv_shows.models import TvShows

class IMDBService():

    @staticmethod
    def get_soup(content):
        return BeautifulSoup(content, 'lxml')

    @staticmethod
    def get_image(item):
        return item.select_one('td.posterColumn img').get('src')

    @staticmethod
    def get_name_and_url(item):
        column = item.select_one('td.titleColumn')
        url = "https://www.imdb.com" + column.select_one('a').get('href')
        name = column.select_one('a').text + " " + column.select_one('span.secondaryInfo').text
        return name, url

    @staticmethod
    def get_rating(item):
        rate = item.select_one('td.imdbRating').text
        try:
            return float(rate)
        except ValueError:
            return float(0)

    def extract_data(self, index, item, _type):
        name, detail_url = self.get_name_and_url(item)
        data = dict(
            image=self.get_image(item),
            name=name,
            rating=self.get_rating(item),
            detail_url=detail_url,
        )
        if _type == 'top_250':
            data.update({'is_top_250': True, 'top_250_order': index + 1})
        else:
            data.update({'is_most_popular': True, 'most_popular_order': index + 1})
        return data

    def top_250_movies(self):
        css = 'table[data-caller-name="chart-top250movie"] tbody.lister-list tr'
        client = IMDBClient()
        response = client.top_250_movies()
        soup = self.get_soup(response.content)
        items = soup.select(css)
        for index, item in enumerate(items):
            movie = self.extract_data(index, item, _type='top_250')
            self.save_object(model=Movie, data=movie)

    def most_popular_movies(self):
        css = 'table[data-caller-name="chart-moviemeter"] tbody.lister-list tr'
        client = IMDBClient()
        response = client.most_popular_movies()
        soup = self.get_soup(response.content)
        items = soup.select(css)
        for index, item in enumerate(items):
            movie = self.extract_data(index, item, _type='most_popular')
            self.save_object(model=Movie, data=movie)

    def top_250_tv_shows(self):
        css = 'table[data-caller-name="chart-top250tv"] tbody.lister-list tr'
        client = IMDBClient()
        response = client.top_250_tv_shows()
        soup = self.get_soup(response.content)
        items = soup.select(css)
        for index, item in enumerate(items):
            tv_show = self.extract_data(index, item, _type='top_250')
            self.save_object(model=TvShows, data=tv_show)

    def most_popular_tv_shows(self):
        css = 'table[data-caller-name="chart-tvmeter"] tbody.lister-list tr'
        client = IMDBClient()
        response = client.most_popular_tv_shows()
        soup = self.get_soup(response.content)
        items = soup.select(css)
        for index, item in enumerate(items):
            tv_show = self.extract_data(index, item, _type='most_popular')
            self.save_object(model=TvShows, data=tv_show)

    @staticmethod
    def save_object(model, data):
        instance = model.objects.filter(name=data.get('name'))
        if instance.exists():
            instance.update(**data)
        else:
            model.objects.create(**data)
