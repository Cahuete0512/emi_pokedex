from django import forms
from .models import Equipe
from .models import Pokemon


class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ('name', 'pokemons')

        name = forms.CharField()
        pokemons = forms.ModelMultipleChoiceField(
            queryset=Pokemon.objects.all(),
            widget=forms.SelectMultiple
        )
