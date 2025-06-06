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
    annee_sortie = models.PositiveIntegerField()
    realisateur = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    acteurs = models.ManyToManyField(Acteur, through='Role')
    affiche = models.ImageField(upload_to='affiches/', blank=True, null=True)

    def __str__(self):
        return self.titre

    def moyenne_notes(self):
        notes = self.commentaires.all()
        if notes.exists():
            return round(sum([c.note for c in notes]) / len(notes), 1)
        return None

    def meilleur_commentaire(self):
        return self.commentaires.order_by('-note').first()

    def pire_commentaire(self):
        return self.commentaires.order_by('note').first()

class Role(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.acteur} dans {self.film}"

class Commentaire(models.Model):
    film = models.ForeignKey(Film, related_name='commentaires', on_delete=models.CASCADE)
    texte = models.TextField()
    note = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire ({self.note}/5)"
