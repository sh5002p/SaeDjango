from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Film, Acteur, Categorie, Commentaire
from .forms import FilmForm, ActeurForm, CategorieForm, CommentaireForm
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

    def form_valid(self, form):
        film_id = self.kwargs['film_id']
        form.instance.film_id = film_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail_film', kwargs={'pk': self.kwargs['film_id']})