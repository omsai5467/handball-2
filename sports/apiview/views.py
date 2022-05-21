from django.shortcuts import render
from players.models import playerdata
# Create your views here.
from django.http import JsonResponse
import json  
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def getPlayers(request):
	if request.method == "GET":
		information = playerdata.objects.all()
		jsoninformation = serializers.serialize('json', information)
		return JsonResponse({"players":jsoninformation})
		# serialized_queryset = serializers.serialize('json', some_queryse
@csrf_exempt
def getPlayer(request,play):
	if request.method == "GET":
		player = [playerdata.objects.get(playerid =play )]
		jsoninformation = serializers.serialize('json', player)
		return JsonResponse({"player":jsoninformation})
	if request.method == "DELETE":
		try:
			player = playerdata.objects.get(playerid =play )
			player.delete()
		except:
			return JsonResponse({"status":"player Not Found"})
		return JsonResponse({"status":"success"})

	if request.method == "POST":
		# print(request['body'])
		# print(request.body)
		jsom = json.loads(request.body)
		print(jsom.data)
		return JsonResponse({"om":"om"})




