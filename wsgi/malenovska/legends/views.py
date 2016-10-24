from django.views import generic

from .models import Legend


class LegendView(generic.ListView):
    template_name = 'legends.html'
    context_object_name = 'legends_list'

    def get_queryset(self):
        return Legend.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(LegendView, self).get_context_data(**kwargs)
        context['page_name'] = AboutWidget.objects.get(
            identifier='page_name').name
        return context
