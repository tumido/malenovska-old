from django import forms
from .models import Player, Race

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['nick', 'name', 'surname', 'age', 'race', 'group']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['nick'].widget.attrs.update({'label': 'Přezdívka', 'placeholder': 'Mirek', 'class':'form-control'})
        self.fields['name'].widget.attrs.update({'label': 'Jméno', 'placeholder': 'Mirek', 'class':'form-control'})
        self.fields['surname'].widget.attrs.update({'label': 'Příjmení', 'placeholder': 'Dušín', 'class':'form-control'})
        self.fields['age'].widget.attrs.update({'label': 'Věk', 'class':'form-control'})
        self.fields['age'].initial = 18
        self.fields['race'].widget.attrs.update({'label': 'Rasa', 'class':'form-control'})
        self.fields['race'].queryset = Race.objects.filter(active=True).only('id', 'name')
        self.fields['group'].widget.attrs.update({'label': 'Skupina', 'placeholder': 'Rychlé Šípy', 'class':'form-control'})
