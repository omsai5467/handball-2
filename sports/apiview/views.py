from django.shortcuts import render
from players.models import playerdata
# Create your views here.
from django.http import JsonResponse
import json  
from .models import updates,matches,leagues,allaccouncements,StateAssociations,BoardManageMent,SelectionCommittee,AthletesCommission
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def getPlayers(request):
	if request.method == "GET":
		information = playerdata.objects.all()
		f=["playerid","team","firstname","lastname","fathername","address","phonenumber","Email","gender","age","city","state","photo","adhar","birth","Height","Goals","Wins","Nationality","JersyNo","Weight","GamesNo","Losses"]
		jsoninformation = serializers.serialize('python', information)
		actual_data = [d['fields'] for d in jsoninformation]
		# jsoninformation.insert(0,{"result":len(jsoninformation),"msg":"DataFound"}) 
		# print(type(actual_data))
		# actual_data["msg"] = "Data Found"
		information = {"msg" :"DataFound","status_code":200,"result":len(jsoninformation),"data":actual_data}
		output = json.dumps(information)

		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# serialized_queryset = serializers.serialize('json', some_queryse
@csrf_exempt
def getPlayer(request,play):
	if request.method == "GET":
		player = [playerdata.objects.get(playerid =play )]

		jsoninformation = serializers.serialize('json', player)
		obj = json.loads(json.loads(json.dumps(jsoninformation)))
		output = json.dumps(obj)
		return HttpResponse(output, content_type='application/json')
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
		# jsoninformation = serializers.serialize('json', up)
		jsoninformation = serializers.serialize('python', up)
		actual_data = [d['fields'] for d in jsoninformation]
		actual_data.insert(0,{"result":len(actual_data)})## = f"{len(actual_data)}"

		actual_data.insert(0,{"msg":"data found"}) 
		# actual_data["result"] = f"{len(actual_data)}"

		# actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})


@csrf_exempt
def StateViseAssociations(request,state):
	if request.method=="GET":
		assosiations = StateAssociations.objects.all().filter(state=state)
		jsoninformation = serializers.serialize('python', assosiations)
		actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})

@csrf_exempt
def StateAssociationsAll(request):
	if request.method=="GET":
		assosiations = StateAssociations.objects.all()
		jsoninformation = serializers.serialize('python', assosiations)
		actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})


@csrf_exempt
def getAllBoardMembers(request):
	if request.method=="GET":
		board = BoardManageMent.objects.all()
		jsoninformation = serializers.serialize('python', board)
		actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})



def getAllSelectionCommittee(request):
	if request.method=="GET":
		board = SelectionCommittee.objects.all()
		jsoninformation = serializers.serialize('python', board)
		actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})

def getAthletesCommission(request):
	if request.method=="GET":
		board = AthletesCommission.objects.all()
		jsoninformation = serializers.serialize('python', board)
		actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})

def upmatches(request):
	if request.method=="GET":
		m = matches.objects.all()
		jsoninformation = serializers.serialize('python', m)
		actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})
def accouncements(request):
	if request.method=="GET":
		m = allaccouncements.objects.all()
		jsoninformation = serializers.serialize('python', allaccouncements)
		actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})


def upcomeingLeagues(request):
	if request.method=="GET":
		m = leagues.objects.all()
		jsoninformation = serializers.serialize('python', m)
		actual_data = [d['fields'] for d in jsoninformation]
		output = json.dumps(actual_data)
		# return JsonResponse({"players":output})
		return HttpResponse(output, content_type='application/json')
		# return JsonResponse({"data":jsoninformation})

		