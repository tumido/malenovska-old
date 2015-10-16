from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from string import ascii_uppercase

from .models import News, Race, Player, Legend, AboutWidget, DateOptions, TextOptions, MapPoints, Harmonogram
from .forms import RegisterForm

def enable_form():
    # funcion which tells wheter it's the time to show users the registration form or not
    start = timezone.localtime(DateOptions.objects.get(identifier='register_unlock').date)
    stop = timezone.localtime(DateOptions.objects.get(identifier='register_lock').date)
    return start < timezone.now() < stop


class RegisterView(generic.CreateView):
    template_name = 'register.html'
    model = Player
    form_class = RegisterForm
    success_url = '/register/'

    def get_form(self, form_class=None):
        if not enable_form():
            return None
        return super(RegisterView, self).get_form(form_class)


    def form_valid(self, form):
        player = form.save(commit=False)
        if len(Player.objects.filter(race=player.race)) + 1 > player.race.limit:
            form.errors['overlimit'] = 'prekrocen limit pro rasu'
            return self.form_invalid(form)
        player.ip = self.request.META['REMOTE_ADDR']
        player.date = timezone.localtime(timezone.now())
        player.save()
        messages.success(self.request, 'Registrace byla ůspěšná')
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        if 'overlimit' in form.errors.keys():
            messages.error(self.request, 'Neregistrováno: Překročen limit strany')
        elif '__all__' in form.errors.keys():
            messages.error(self.request, 'Neregistrováno: Takový bojovník již existuje')
        else:
            messages.error(self.request, 'Neregistrováno: Zkontrolujte údaje')
        return super(RegisterView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        for text in AboutWidget.objects.filter(identifier__contains='register'):
            context[text.identifier] = text.text
        context['registration_open'] = True

        races = Race.objects.filter(active=True).order_by('fraction', 'name')
        context['players_list'] = [(r, Player.objects.filter(race=r.id).order_by('surname')) for r in races]

        context['after_register_open'] = timezone.localtime(DateOptions.objects.get(identifier='register_unlock').date) < timezone.now()
        context['page_name'] = AboutWidget.objects.get(identifier='page_name').name

        return context


class LegendView(generic.ListView):
    template_name = 'legends.html'
    context_object_name = 'legends_list'

    def get_queryset(self):
        return Legend.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(LegendView, self).get_context_data(**kwargs)
        context['page_name'] = AboutWidget.objects.get(identifier='page_name').name
        return context


class WorldView(generic.ListView):
    template_name = 'world.html'
    context_object_name = 'races'

    def get_queryset(self):
        return Race.objects.filter(active=True).exclude(description='').order_by('fraction', 'name')

    def get_context_data(self, **kwargs):
        context = super(WorldView, self).get_context_data(**kwargs)
        text = AboutWidget.objects.get(identifier='world_characteristics')
        context[text.identifier] = text.text
        context['page_name'] = AboutWidget.objects.get(identifier='page_name').name
        return context


class InfoView(generic.ListView):
    template_name = 'info.html'
    context_object_name = 'dates'

    def get_queryset(self):
        # get data - time based
        return DateOptions.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        # get data - text based
        for text in AboutWidget.objects.filter(identifier__contains='info'):
            context[text.identifier] = text.text
        # import also the text beside the info panels
        context['texts'] = TextOptions.objects.filter(identifier__contains='important')
        # import map coordinates and point names for map markers
        context['map_points'] = list()
        for i,point in enumerate(MapPoints.objects.all().order_by('id')):
            ch = ascii_uppercase[i]
            context['map_points'].append([ch, point.title,
                                               "{0},{1}".format(point.long, point.lat)])
        context['page_name'] = AboutWidget.objects.get(identifier='page_name').name

        # show contact info (identifier starts with 'contact_')
        contacts = TextOptions.objects.filter(identifier__contains='contact_').order_by('-name')
        # take just the last part of the identifier which is matched to thee displayed icon
        context['contacts'] = { o.identifier.split('_')[-1]: {'name': o.name,
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
            context['contacts']['at']['email'] = "var email =\"" + encrypt +"\".replace(/./g, function(c){return String.fromCharCode(c=c.charCodeAt(0)-3);});"
        # last but not least - harmonogram
        context['harmonogram'] = Harmonogram.objects.all().order_by('time_start')
        return context


class RulesView(generic.ListView):
    template_name = 'rules.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(RulesView, self).get_context_data(**kwargs)
        text = AboutWidget.objects.get(identifier='rules')
        context[text.identifier] = text.text
        context['page_name'] = AboutWidget.objects.get(identifier='page_name').name
        return context


class NewsView(generic.ListView):
    template_name = 'news.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return News.objects.filter(date__lt=timezone.now()).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        text = AboutWidget.objects.get(identifier='page_name')
        context[text.identifier] = text
        return context
