from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from .models import Film, Acteur, Categorie, Commentaire, Personne, Usager
from .forms import FilmForm, ActeurForm, CategorieForm, CommentaireForm, PersonneForm, UsagerForm


# === Films ===
class ListeFilms(ListView):
    model = Film
    template_name = "films/liste_films.html"
    context_object_name = "films"

class DetailFilm(DetailView):
    model = Film
    template_name = "films/detail_film.html"
    context_object_name = "film"

class AjoutFilm(CreateView):
    model = Film
    form_class = FilmForm
    template_name = "films/formulaire_film.html"
    success_url = reverse_lazy("liste_films")


class ModifierFilm(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = "films/formulaire_film.html"
    success_url = reverse_lazy("liste_films")

class SupprimerFilm(DeleteView):
    model = Film
    template_name = "films/film_confirm_delete.html"
    success_url = reverse_lazy("liste_films")

# === Acteurs ===
class ListeActeurs(ListView):
    model = Acteur
    template_name = "films/liste_acteurs.html"
    context_object_name = "acteurs"

class DetailActeur(DetailView):
    model = Acteur
    template_name = "films/detail_acteur.html"
    context_object_name = "acteur"

class AjoutActeur(CreateView):
    model = Acteur
    form_class = ActeurForm
    template_name = "films/formulaire_acteur.html"
    success_url = reverse_lazy("liste_acteurs")

# === Catégories ===
class ListeCategories(ListView):
    model = Categorie
    template_name = "films/liste_categories.html"
    context_object_name = "categories"

class DetailCategorie(DetailView):
    model = Categorie
    template_name = "films/detail_categorie.html"
    context_object_name = "categorie"

class AjoutCategorie(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "films/formulaire_categorie.html"
    success_url = reverse_lazy("liste_categories")
class AjoutCommentaire(CreateView):
    model = Commentaire
    form_class = CommentaireForm
    template_name = "films/formulaire_commentaire.html"

    def dispatch(self, request, *args, **kwargs):
        self.film = get_object_or_404(Film, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.film = self.film
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail_film", args=[self.film.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film'] = self.film
        return context

class AjoutPersonne(CreateView):
    model = Personne
    form_class = PersonneForm
    template_name = 'films/formulaire_personne.html'
    success_url = reverse_lazy('liste_films')
class AjoutUsager(CreateView):
    model = Usager
    form_class = UsagerForm
    template_name = "films/formulaire_usager.html"
    success_url = reverse_lazy("liste_films")  # Redirection après enregistrement

class ModifierActeur(UpdateView):
    model = Acteur
    form_class = ActeurForm
    template_name = "films/formulaire_acteur.html"
    success_url = reverse_lazy("liste_acteurs")

class SupprimerActeur(DeleteView):
    model = Acteur
    template_name = "films/acteur_confirm_delete.html"
    success_url = reverse_lazy("liste_acteurs")

class ModifierCategorie(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "films/formulaire_categorie.html"
    success_url = reverse_lazy("liste_categories")

class SupprimerCategorie(DeleteView):
    model = Categorie
    template_name = "films/categorie_confirm_delete.html"
    success_url = reverse_lazy("liste_categories")

