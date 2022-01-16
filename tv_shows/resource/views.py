from django.views.generic import TemplateView
from tv_shows.models import TvShows


class Top250TvShowsView(TemplateView):
    template_name = "index.html"
    queryset = TvShows.objects.filter(is_top_250=True).order_by('top_250_order')

    def get_context_data(self, **kwargs):
        context = super(Top250TvShowsView, self).get_context_data(**kwargs)
        context['items'] = self.queryset
        context['selector'] = 'top_250'
        return context


class MostPopularTvShowsView(TemplateView):
    template_name = "index.html"
    queryset = TvShows.objects.filter(is_most_popular=True).order_by(
        'most_popular_order')

    def get_context_data(self, **kwargs):
        context = super(MostPopularTvShowsView, self).get_context_data(**kwargs)
        context['items'] = self.queryset
        context['selector'] = 'most_popular'
        return context
