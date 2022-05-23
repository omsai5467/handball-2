from django.shortcuts import render
from players.models import playerdata
# Create your views here.
from django.http import JsonResponse
import json  
from .models import updates,StateAssociations,BoardManageMent,SelectionCommittee,AthletesCommission
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



@csrf_exempt
def latestUpdates(request):
	if request.method=="GET":
		up = updates.objects.all()
		jsoninformation = serializers.serialize('json', up)
		return JsonResponse({"data":jsoninformation})


@csrf_exempt
def StateViseAssociations(request,state):
	if request.method=="GET":
		assosiations = StateAssociations.objects.all().filter(state=state)
		jsoninformation = serializers.serialize('json', assosiations)
		return JsonResponse({"data":jsoninformation})

@csrf_exempt
def StateAssociationsAll(request):
	if request.method=="GET":
		assosiations = StateAssociations.objects.all()
		jsoninformation = serializers.serialize('json', assosiations)
		return JsonResponse({"data":jsoninformation})


@csrf_exempt
def getAllBoardMembers(request):
	if request.method=="GET":
		board = BoardManageMent.objects.all()
		jsoninformation = serializers.serialize('json', board)
		return JsonResponse({"data":jsoninformation})



def getAllSelectionCommittee(request):
	if request.method=="GET":
		board = SelectionCommittee.objects.all()
		jsoninformation = serializers.serialize('json', board)
		return JsonResponse({"data":jsoninformation})

def getAthletesCommission(request):
	if request.method=="GET":
		board = AthletesCommission.objects.all()
		jsoninformation = serializers.serialize('json', board)
		return JsonResponse({"data":jsoninformation})
