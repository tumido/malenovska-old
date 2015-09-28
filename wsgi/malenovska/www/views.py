from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages

from .models import Race, Player, Legend, AboutWidget
from .forms import RegisterForm

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'race_list'

    def get_queryset(self):
        return Race.objects.order_by('-name')

class RegisterView(generic.CreateView):
    template_name = 'register.html'
    model = Player
    form_class = RegisterForm
    success_url = '/register/'

    def form_valid(self, form):
        player = form.save(commit=False)
        if len(Player.objects.filter(race=player.race)) + 1 >= player.race.limit:
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

        races = Race.objects.filter(active=True).order_by('-fraction', '-name')
        context['players_list'] = [(r, Player.objects.filter(race=r.id).order_by('-surname')) for r in races]

        return context

class LegendView(generic.ListView):
    template_name = 'legends.html'
    context_object_name = 'legends_list'

    def get_queryset(self):
        return Legend.objects.order_by('-id')

class WorldView(generic.ListView):
    template_name = 'world.html'
    context_object_name = 'races'

    def get_queryset(self):
        return Race.objects.filter(active=True).order_by('-fraction', '-name')

    def get_context_data(self, **kwargs):
        context = super(WorldView, self).get_context_data(**kwargs)
        text = AboutWidget.objects.get(identifier='world_characteristics')
        context[text.identifier] = text.text
        return context


class InfoView(generic.ListView):
    template_name = 'info.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        for text in AboutWidget.objects.filter(identifier__contains='info'):
            context[text.identifier] = text.text
        return context

class RulesView(generic.ListView):
    template_name = 'rules.html'

    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super(RulesView, self).get_context_data(**kwargs)
        text = AboutWidget.objects.get(identifier='rules')
        context[text.identifier] = text.text
        return context
