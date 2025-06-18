from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Acteur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='acteurs/', blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Film(models.Model):
    titre = models.CharField(max_length=200)
    realisateur = models.CharField(max_length=100, blank=True)
    acteurs = models.ManyToManyField('Acteur', blank=True)
    annee_sortie = models.DateField(verbose_name="Date de sortie")
    synopsis = models.TextField(blank=True)
    affiche = models.ImageField(upload_to='affiches/', blank=True, null=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre

    def moyenne_notes(self):
        notes = self.commentaires.all()
        if notes.exists():
            return round(sum([c.note for c in notes]) / len(notes), 1)
        return None

    @property
    def meilleur_commentaire(self):
        return self.commentaires.order_by('-note').first()

    @property
    def pire_commentaire(self):
        return self.commentaires.order_by('note').first()

class Commentaire(models.Model):
    film = models.ForeignKey(Film, related_name='commentaires', on_delete=models.CASCADE)
    personne = models.ForeignKey('Personne', on_delete=models.CASCADE)
    texte = models.TextField()
    note = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire ({self.note}/20) par {self.personne}"


class Personne(AbstractUser):
    TYPES = [
        ('pro', 'Professionnel'),
        ('ama', 'Amateur'),
    ]
    pseudo = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    type = models.CharField(max_length=3, choices=TYPES)

    USERNAME_FIELD = 'pseudo'
    REQUIRED_FIELDS = ['email', 'nom', 'prenom']

    def __str__(self):
        return self.pseudo



class Usager(models.Model):
    TYPE_CHOICES = [
        ('pro', 'Professionnel'),
        ('amateur', 'Amateur'),
    ]

    pseudo = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.pseudo
