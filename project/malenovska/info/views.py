"""View for generic info about Malenovska."""
from django.views import generic
from string import ascii_uppercase

from .models import TextOptions, Harmonogram, MapPoints, ExtraFiles
from general.models import DateOptions, AboutWidget


class InfoView(generic.ListView):
    """The view class for info page."""

    template_name = 'info.html'
    context_object_name = 'dates'

    def get_queryset(self):
        """Base the view upon the dates."""
        return DateOptions.objects.all()

    def get_context_data(self, **kwargs):
        """Load the template with all other data."""
        context = super(InfoView, self).get_context_data(**kwargs)
        # get data - text based
        for text in AboutWidget.objects.filter(identifier__contains='info'):
            print(text.identifier)
            context[text.identifier] = text.text
        # import also the text beside the info panels
        context['texts'] = TextOptions.objects.filter(
            identifier__contains='important')
        # import map coordinates and point names for map markers
        context['map_points'] = list()
        for i, point in enumerate(MapPoints.objects.all().order_by('id')):
            ch = ascii_uppercase[i]
            context['map_points'].append([
                ch,
                point.title,
                "{0},{1}".format(point.long, point.lat)
            ])
        context['page_name'] = AboutWidget.objects.get(
            identifier='page_name').name

        # show contact info (identifier starts with 'contact_')
        contacts = TextOptions.objects.filter(
            identifier__contains='contact_').order_by('-name')
        # take just the last part of the identifier which is matched to thee
        # displayed icon
        context['contacts'] = {o.identifier.split('_')[-1]: {'name': o.name,
                                                             'text': o.text}
                               for o in contacts}

        # if the e-mail address is listed here, encrypt it to avoid spam bots
        # for now it's done by Javascript by shifting the char code a bit
        if 'at' in context['contacts']:
            email = context['contacts']['at']['text']
            email = 'mailto:' + email
            encrypt = ''
            for i in email:
                encrypt += chr(ord(i) + 3)
            context['contacts']['at']['text'] = "mailto:"
            context['contacts']['at']['email'] = "var email =\"" + encrypt + \
                "\".replace(/./g, function(c){return String.fromCharCode(" + \
                "c=c.charCodeAt(0)-3);});"

        # last but not least - harmonogram
        context['harmonogram'] = \
            Harmonogram.objects.all().order_by('time_start')

        # add acknowledgement for youngsters
        context['files'] = ExtraFiles.objects.all().order_by('name')

        return context
