from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages

from .models import Race, Player, Legend
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
        player.ip = self.request.META['REMOTE_ADDR']
        player.date = timezone.localtime(timezone.now())
        player.save()
        messages.success(self.request, 'Registrace byla ůspěšná')
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        if '__all__' in form.errors.keys():
            messages.error(self.request, 'Neregistrováno: Takový bojovník již existuje')
        else:
            messages.error(self.request, 'Neregistrováno: Zkontrolujte údaje')
        return super(RegisterView, self).form_invalid(form)

class LegendView(generic.ListView):
    template_name = 'legends.html'
    context_object_name = 'legends_list'

    def get_queryset(self):
        return Legend.objects.order_by('-id')
