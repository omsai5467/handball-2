from re import M
from django.db import models

# Create your models here.


class blogs(models.Model):
    img = models.ImageField(upload_to="blogs/",null=True, blank=True)
    name = models.CharField(max_length=50,blank=True)
    createdAt= models.DateTimeField(auto_now_add=True)
    Dis = models.TextField()
    def __str__(self):
        return self.name


class matches(models.Model):
    team1=models.CharField(max_length=50)
    team2=models.CharField(max_length=50)
    createdAt=models.DateTimeField(auto_now_add=True)
    matchdate=models.DateTimeField(blank=False)
    location=models.CharField(max_length=100)
    discription=models.TextField()
    def __str__(self):
        return f"{self.team1}VS{self.team2}"