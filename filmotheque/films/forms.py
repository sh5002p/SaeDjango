from django import forms
from .models import Film, Acteur, Categorie, Commentaire
from django.contrib.auth.forms import UserCreationForm
from .models import Personne
from .models import Film, Acteur, Categorie, Commentaire, Usager


class FilmForm(forms.ModelForm):
    annee_sortie = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date de sortie"
    )
    realisateur = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nom du réalisateur'}),
        label="Réalisateur",
        required=False
    )

    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'acteurs': forms.SelectMultiple(attrs={'size': 6}),
        }

class ActeurForm(forms.ModelForm):
    class Meta:
        model = Acteur
        fields = '__all__'

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['personne', 'note', 'texte']
        widgets = {
            'note': forms.NumberInput(attrs={'min': 0, 'max': 20}),
        }


class PersonneForm(UserCreationForm):
    class Meta:
        model = Personne
        fields = ['pseudo', 'nom', 'prenom', 'mail', 'type', 'password1', 'password2']

class UsagerForm(forms.ModelForm):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usager
        fields = '__all__'
