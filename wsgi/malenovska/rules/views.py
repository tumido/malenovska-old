"""Rules view."""
from django.views import generic

from general.models import AboutWidget


class RulesView(generic.ListView):
    """The view containing all Rules."""

    template_name = 'rules.html'

    def get_queryset(self):
        """Fake query to DB, rules are currently stored elsewhere."""
        return []

    def get_context_data(self, **kwargs):
        """Fill the template."""
        context = super(RulesView, self).get_context_data(**kwargs)
        text = AboutWidget.objects.get(identifier='rules')
        context[text.identifier] = text.text
        context['page_name'] = AboutWidget.objects.get(
            identifier='page_name').name
        return context
