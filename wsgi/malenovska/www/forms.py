from django import forms
from .models import Player

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['nick', 'name', 'surname', 'age', 'race']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['nick'].widget.attrs.update({'label': 'Přezdívka', 'placeholder': 'Krutej válečník', 'class':'form-control'})
        self.fields['name'].widget.attrs.update({'label': 'Jméno', 'placeholder': 'Jan', 'class':'form-control'})
        self.fields['surname'].widget.attrs.update({'label': 'Příjmení', 'placeholder': 'Novák', 'class':'form-control'})
        self.fields['age'].widget.attrs.update({'label': 'Věk', 'class':'form-control'})
        self.fields['age'].initial = 15
        self.fields['race'].widget.attrs.update({'label': 'Rasa', 'class':'form-control'})
