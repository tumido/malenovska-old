"""Register a Player for Malenovska."""
from django import forms
from .models import Player
from races.models import Race


class RegisterForm(forms.ModelForm):
    """Form for creating Player model."""

    class Meta:
        """"Django Meta class for form."""

        model = Player
        fields = ['nick', 'name', 'surname', 'email', 'age', 'race', 'group']

    def __init__(self, *args, **kwargs):
        """Initialize form fields widgets."""
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['nick'].widget.attrs.update({
            'label': 'Přezdívka',
            'placeholder': 'Mirek'
        })

        self.fields['name'].widget.attrs.update({
            'label': 'Jméno',
            'placeholder': 'Mirek'
        })

        self.fields['surname'].widget.attrs.update({
            'label': 'Příjmení',
            'placeholder': 'Dušín'
        })

        self.fields['email'].widget.attrs.update({
            'label': 'E-mail',
            'placeholder': 'mirek@rychlesipy.cz'
        })

        self.fields['age'].widget.attrs.update({'label': 'Věk'})
        self.fields['age'].initial = 18

        self.fields['race'].widget.attrs.update({'label': 'Rasa'})
        self.fields['race'].queryset = Race.objects.filter(
            active=True).only('id', 'name')

        self.fields['group'].widget.attrs.update({
            'label': 'Skupina',
            'placeholder': 'Rychlé Šípy'
        })

        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({
                'required': self.fields[field].required,
                'title': '',
                'class': 'form-control'
            })
