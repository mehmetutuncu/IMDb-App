from django.views.generic import TemplateView
from movies.models import Movie


class Top250MoviesView(TemplateView):
    template_name = "index.html"
    queryset = Movie.objects.filter(is_top_250=True).order_by('top_250_order')

    def get_context_data(self, **kwargs):
        context = super(Top250MoviesView, self).get_context_data(**kwargs)
        context['items'] = self.queryset
        context['selector'] = 'top_250'
        return context


class MostPopularMoviesView(TemplateView):
    template_name = "index.html"
    queryset = Movie.objects.filter(is_most_popular=True).order_by(
        'most_popular_order')

    def get_context_data(self, **kwargs):
        context = super(MostPopularMoviesView, self).get_context_data(**kwargs)
        context['items'] = self.queryset
        context['selector'] = 'most_popular'
        return context
