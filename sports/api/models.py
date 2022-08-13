from re import M
from django.db import models

# Create your models here.

class upcomeing(models.Model):
    logoofTeam1  = models.ImageField(upload_to="teams/")
    logoofTeam2 = models.ImageField(upload_to="blogs/")
    team1=models.CharField(max_length=50)
    team2=models.CharField(max_length=50)
    createdAt=models.DateTimeField()
    dis = models.TextField()
    




status = (
    ("trending","trending"),
    ("recent","recent"),
    )
class blogs(models.Model):
    img = models.ImageField(upload_to="blogs/",null=True, blank=True)
    name = models.CharField(max_length=50,blank=True)
    createdAt = models.DateField(auto_now_add=True)
    Dis = models.TextField()
    status = models.CharField(max_length=50,choices=status)
    def __str__(self):
        return self.name


class matches(models.Model):
    logoofTeam1  = models.ImageField(upload_to="teams/")
    logoofTeam2 = models.ImageField(upload_to="blogs/")
    team1=models.CharField(max_length=50)
    team2=models.CharField(max_length=50)
    createdAt=models.DateTimeField(auto_now_add=True)
    matchdate=models.DateTimeField(blank=False)
    location=models.CharField(max_length=100)
    discription=models.TextField()
    matchCompleated = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.team1}VS{self.team2}"



class videos(models.Model):
    img=models.ImageField(upload_to="videos/",blank=True)
    link =  models.URLField(max_length = 500)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name



class pointsTable(models.Model):
    team = models.CharField(max_length=50)
    PLD =  models.IntegerField(blank=False, null=False)
    wins = models.IntegerField(blank=False, null=False)
    LOSS =  models.IntegerField(blank=False, null=False)
    points =  models.IntegerField(blank=False, null=False)



class NEWS(models.Model):
    img = models.ImageField(upload_to="news/")
    name = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    discription = models.TextField()
    def __str__(self):
        return self.name



class quiz(models.Model):
    name = models.CharField(max_length=50)
    ans = models.IntegerField(default=1)
    def __str__(self):
        return self.q


