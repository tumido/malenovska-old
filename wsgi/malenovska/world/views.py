from django.views import generic
from .models import Race

from general.models import AboutWidget


class WorldView(generic.ListView):
    """
    Display all the World specific data

    Show all the general info along with Races description
    """
    template_name = 'world.html'
    context_object_name = 'races'

    def get_queryset(self):
        return Race.objects.filter(active=True).exclude(
            description='').order_by('fraction', 'name')

    def get_context_data(self, **kwargs):
        context = super(WorldView, self).get_context_data(**kwargs)
        text = AboutWidget.objects.get(identifier='world_characteristics')
        context[text.identifier] = text.text
        context['page_name'] = AboutWidget.objects.get(
            identifier='page_name').name
        return context
