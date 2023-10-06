from django.contrib.auth.models import User
from django.db import models

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    haqida = models.TextField()
    def __str__(self):
        return self.nom

class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    tirik = models.BooleanField()
    mamlakat = models.CharField(max_length=100)
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    yili = models.DateField(auto_now_add=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()
