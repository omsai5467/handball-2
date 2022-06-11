
from rest_framework import serializers

from . models import *



class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogs
        fields = ["img","name","createdAt","Dis"]


class matchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = matches
        fields = ["id","team1","team2","matchdate","location","discription"]


class upcomeingSerializer(serializers.ModelSerializer):
    class Meta:
        model = upcomeing
        fields=["team1","team2","id","dis"]

class videosSerializer(serializers.ModelSerializer):
    class Meta:
        model = videos
        fields = ["img","link"]


class blogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogs
        fields=["id","createdAt","name","img","Dis"]



class pointsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = pointsTable
        fields="__all__"


from players.models import playerdata

class playerdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = playerdata
        fields = ["playerid","firstname","lastname","photo","DateOfBirth","state","Goals","Weight",]



class newsSerializer(serializers.ModelSerializer):
    class Meta:
        model=NEWS
        fields = "__all__"


class SinglePlayerdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = playerdata
        fields = ["playerid","firstname","lastname","photo","DateOfBirth","state","Goals","Weight",]