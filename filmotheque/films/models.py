from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PROFESSIONNEL = 'PRO'
    AMATEUR = 'AMA'
    TYPE_UTILISATEUR = [
        (PROFESSIONNEL, 'Professionnel'),
        (AMATEUR, 'Amateur'),
    ]

    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    type_utilisateur = models.CharField(max_length=3, choices=TYPE_UTILISATEUR, default=AMATEUR)

    def __str__(self):
        return f"{self.username} ({self.get_type_utilisateur_display()})"


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom


class Acteur(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='acteurs/', null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Film(models.Model):
    titre = models.CharField(max_length=200)
    annee_sortie = models.PositiveIntegerField()
    affiche = models.ImageField(upload_to='affiches/', null=True, blank=True)
    realisateur = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    acteurs = models.ManyToManyField(Acteur, through='FilmActeur')

    def __str__(self):
        return f"{self.titre} ({self.annee_sortie})"

    def moyenne_notes(self, type_utilisateur=None):
        from django.db.models import Avg, Q
        queryset = self.commentaires.all()
        if type_utilisateur:
            queryset = queryset.filter(utilisateur__type_utilisateur=type_utilisateur)
        return queryset.aggregate(Avg('note'))['note__avg'] or 0

    def meilleur_commentaire(self):
        return self.commentaires.order_by('-note').first()

    def pire_commentaire(self):
        return self.commentaires.order_by('note').first()


class FilmActeur(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE)
    nom_role = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('film', 'acteur')

    def __str__(self):
        return f"{self.acteur} dans {self.film}"


class Commentaire(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='commentaires')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    texte = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Commentaire de {self.utilisateur} sur {self.film} ({self.note}/5)"