"""Views for registration of Players."""

from django.views import generic
from django.contrib import messages
from django.utils import timezone

from .models import Player
from .forms import RegisterForm
from world.models import Race
from general.models import DateOptions, AboutWidget


def enable_form():
    """Provide time frame when registration is enabled."""
    start = timezone.localtime(DateOptions.objects.get(
        identifier='register_unlock').date)
    stop = timezone.localtime(DateOptions.objects.get(
        identifier='register_lock').date)
    return start < timezone.now() < stop


class RegisterView(generic.CreateView):
    """Registration page."""

    template_name = 'register.html'
    model = Player
    form_class = RegisterForm
    success_url = '/register/'

    def get_form(self, form_class=None):
        """Get the form that should be displayed."""
        if not enable_form():
            return None
        return super(RegisterView, self).get_form(form_class)

    def form_valid(self, form):
        """
        Proceed with registration when the form passed validation.

        Create user entry and flash message telling the registration was
        accepted.
        """
        player = form.save(commit=False)
        registered_players = len(Player.objects.filter(race=player.race))

        if registered_players + 1 > player.race.limit:
            form.errors['overlimit'] = 'prekrocen limit pro rasu'
            return self.form_invalid(form)

        player.ip = self.request.META['REMOTE_ADDR']
        player.date = timezone.localtime(timezone.now())
        player.save()

        messages.success(self.request, 'Registrace byla úspěšná')
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        """The form validation failed. Let the user know."""
        if 'overlimit' in form.errors.keys():
            messages.error(
                self.request, 'Neregistrováno: Překročen limit strany')
        elif '__all__' in form.errors.keys():
            messages.error(
                self.request, 'Neregistrováno: Takový bojovník již existuje')
        else:
            messages.error(self.request, 'Neregistrováno: Zkontrolujte údaje')
        return super(RegisterView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        """Feed the template with all required DB data to display."""
        # get the context object
        context = super(RegisterView, self).get_context_data(**kwargs)

        # fetch all register related settings
        for text in AboutWidget.objects.filter(
                identifier__contains='register'):
            context[text.identifier] = text.text

        # get list of already registered players
        races = Race.objects.filter(active=True).order_by('fraction', 'name')
        context['players_list'] = [(r, Player.objects.filter(
            race=r.id).order_by('surname')) for r in races]

        # let template know if registration is already over
        reg_close = DateOptions.objects.get(identifier='register_lock').date
        reg_open = DateOptions.objects.get(identifier='register_unlock').date

        context['after_registration'] = reg_close <= timezone.now()
        context['before_registration'] = reg_open >= timezone.now()

        # get title
        context['page_name'] = AboutWidget.objects.get(
            identifier='page_name').name

        print(reg_open)
        return context
