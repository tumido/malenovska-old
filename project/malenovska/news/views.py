"""News view."""
from django.views import generic
from django.utils import timezone

from .models import News
from general.models import DateOptions, AboutWidget


class NewsView(generic.ListView):
    """News view for Malenovska home page."""

    template_name = 'news.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        """List of released news."""
        return News.objects.filter(date__lt=timezone.now()).order_by('-date')

    def get_context_data(self, **kwargs):
        """Data to load for template."""
        context = super(NewsView, self).get_context_data(**kwargs)
        text = AboutWidget.objects.get(identifier='page_name')
        context[text.identifier] = text
        return context
