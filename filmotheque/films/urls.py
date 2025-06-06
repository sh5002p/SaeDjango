from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListeFilms.as_view(), name='liste_films'),
    path('films/<int:pk>/', views.DetailFilm.as_view(), name='detail_film'),
    path('films/ajouter/', views.AjoutFilm.as_view(), name='ajout_film'),

    path('acteurs/', views.ListeActeurs.as_view(), name='liste_acteurs'),
    path('acteurs/ajouter/', views.AjoutActeur.as_view(), name='ajout_acteur'),
    path('acteurs/<int:pk>/', views.DetailActeur.as_view(), name='detail_acteur'),

    path('categories/', views.ListeCategories.as_view(), name='liste_categories'),
    path('categories/ajouter/', views.AjoutCategorie.as_view(), name='ajout_categorie'),
    path('categories/<int:pk>/', views.DetailCategorie.as_view(), name='detail_categorie'),
]
