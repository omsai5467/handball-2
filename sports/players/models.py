from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib import admin
# Create your models here.
from datetime import date
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

class playerdata(models.Model):
    team  = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    fathername=models.CharField(max_length=200)
    address=models.TextField()
    phonenumber=models.CharField(max_length=12)
    Email=models.CharField(max_length=200)
    gender=models.CharField(max_length=20)
    DateOfBirth = models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    photo = models.ImageField(upload_to = "profile/", null=True, blank=True)
    adhar = models.ImageField(upload_to = "aadhar/", null=True, blank=True)
    birth = models.ImageField(upload_to = "birth/", null=True, blank=True)
    playerid = models.CharField(max_length = 500000,blank=True)
    # newly added feilds for application
    Height = models.CharField(max_length=20,null=True, blank=True)
    Goals = models.CharField(max_length=25,null=True, blank=True)
    Wins = models.CharField(max_length=200,null=True, blank=True)
    Nationality = models.CharField(max_length=100,null=True, blank=True)
    JersyNo = models.CharField(max_length=20,null=True, blank=True)
    Weight = models.CharField(max_length=100,null=True, blank=True)
    GamesNo = models.CharField(max_length=500,null=True, blank=True)
    Losses = models.CharField(max_length=500,null=True, blank=True)
    cat= models.IntegerField()

# jun-boys = 0
# seni-boys = 1
# jun-girls = 2
# senior-girls = 3

    def __str__(self):
        return self.playerid
    def get_url(self):
            try:
                if self.photo:
                    return True
            except :
                 return False
    def getaa(self):
        try:
            if self.adhar :
                return True
        except:
            return False




# class play(AbstractUser):
#     username = models.
#     isplayer = models.BooleanField(default=False)

# admin.site.register(play)
