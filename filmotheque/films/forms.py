from django import forms
from .models import Film, Acteur, Categorie, Commentaire

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

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
        exclude = ['film']
