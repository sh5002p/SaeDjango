from django.contrib import admin
from .models import User, Categorie, Acteur, Film, FilmActeur, Commentaire

admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Acteur)
admin.site.register(Film)
admin.site.register(FilmActeur)
admin.site.register(Commentaire)