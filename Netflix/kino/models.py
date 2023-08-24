from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Aktyor(models.Model):
    ism = models.CharField(max_length=30)
    davlat = models.CharField(max_length=50,blank=True)
    jins = models.CharField(max_length=30)
    t_yil = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.ism


class Kino(models.Model):
    nom = models.CharField(max_length=50)
    janr = models.CharField(max_length=30)
    yil = models.DateField(null=True,blank=True)
    aktyorlar = models.ManyToManyField(Aktyor)

    def __str__(self):
        return self.nom


class Tarif(models.Model):
    nom  = models.CharField(max_length=50)
    narx = models.PositiveSmallIntegerField()
    davomiylik = models.CharField(max_length=30)

    def __str__(self):
        return f"Tarif - {self.nom}"


class Izoh(models.Model):
    matn = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sana = models.DateField()
    kino = models.ForeignKey(Kino,on_delete=models.CASCADE)
    baho = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Izoh - {self.kino.nom}ga"