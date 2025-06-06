from django.urls import path
from .views import AjoutCommentaire
from . import views

urlpatterns = [
    # Films
    path('', views.ListeFilms.as_view(), name='liste_films'),
    path('films/<int:pk>/', views.DetailFilm.as_view(), name='detail_film'),
    path('films/ajouter/', views.AjoutFilm.as_view(), name='ajout_film'),
    path('films/<int:pk>/modifier/', views.ModifierFilm.as_view(), name='modif_film'),
    path('films/<int:pk>/supprimer/', views.SupprimerFilm.as_view(), name='suppr_film'),
    path('films/<int:pk>/commentaire/ajouter/', AjoutCommentaire.as_view(), name='ajout_commentaire'),
    path('inscription/', views.AjoutPersonne.as_view(), name='ajout_personne'),
    path('usagers/ajouter/', views.AjoutUsager.as_view(), name='ajout_usager'),
    path('personnes/ajouter/', views.AjoutPersonne.as_view(), name='ajout_personne'),


    # Acteurs
    path('acteurs/', views.ListeActeurs.as_view(), name='liste_acteurs'),
    path('acteurs/ajouter/', views.AjoutActeur.as_view(), name='ajout_acteur'),
    path('acteurs/<int:pk>/', views.DetailActeur.as_view(), name='detail_acteur'),

    # Catégories
    path('categories/', views.ListeCategories.as_view(), name='liste_categories'),
    path('categories/ajouter/', views.AjoutCategorie.as_view(), name='ajout_categorie'),
    path('categories/<int:pk>/', views.DetailCategorie.as_view(), name='detail_categorie'),
]
