from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Film, Acteur, Categorie, Commentaire, User, FilmActeur
from .formulaires import (FormulaireFilm, FormulaireActeur, FormulaireCategorie,
                          FormulaireCommentaire, FormulaireUtilisateur, FormulaireImportFilm)
import csv
import json
from io import TextIOWrapper


class VueListeFilms(ListView):
    model = Film
    template_name = 'films/liste_films.html'
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context


class VueDetailFilm(DetailView):
    model = Film
    template_name = 'films/detail_film.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.object
        context['formulaire_commentaire'] = FormulaireCommentaire()
        context['commentaires'] = film.commentaires.all()
        context['moyenne_pro'] = film.moyenne_notes(User.PROFESSIONNEL)
        context['moyenne_amateur'] = film.moyenne_notes(User.AMATEUR)
        context['meilleur_commentaire'] = film.meilleur_commentaire()
        context['pire_commentaire'] = film.pire_commentaire()
        return context

