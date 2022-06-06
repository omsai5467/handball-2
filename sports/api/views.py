from django.shortcuts import render
from . models import *
# Create your views here.
# from rest_framework import status
from rest_framework import status
from players.models import playerdata
from . serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def home(request):
	fixtures = matches.objects.all().filter(matchCompleated=False).order_by("-id")[:5]  
	fixtures = matchesSerializer(fixtures, many=True)
	upcoming = upcomeing.objects.all()[:2]
	upcoming = upcomeingSerializer(upcoming,many=True)
	v = videos.objects.all()
	vi = videosSerializer(v,many=True)
	blog = blogs.objects.all().filter().order_by("-id")[:3]
	b = blogsSerializer(blog,many=True)
	# pointsTableSerializer
	p = pointsTable.objects.all().filter().order_by("-points")
	p = pointsTableSerializer(p,many=True)

	context = {
			"status_code":200,
			"msg":"DataFound",
			"upcomeingMatches":upcoming.data,
			"fixtures":fixtures.data,
			"videos":vi.data,
			"blog":b.data,
			"pointsTable":p.data,	
	}
	return Response(context)



@api_view(["GET"])
def blogposts(request):
	b = blogs.objects.all().filter().order_by("-id")
	latest = blogs.objects.all().filter().order_by("-id")[:1]
	recent = blogs.objects.all().filter().order_by("-id")[:]
	trending = blogs.objects.all().filter(status="trending").order_by("-id")[:3]
	l = blogsSerializer(latest,many=True)
	r=blogsSerializer(recent,many=True)
	t=blogsSerializer(trending,many=True)
	context={
	"status_code":200,
	"msg":"DataFound",
	
		"latest":l.data,
		"recent":r.data,
		"trending":t.data
		
	}
	return Response(context)


count = 0
def allPlayers():
	pl=playerdata.objects.all()
	return pl

PLAYERS = allPlayers()

@api_view(["POST"])
def getPlayers(request):
	# print()
	try:
		start=request.data["start"]
		end = request.data["end"]
		# if start == int and end == int :
		global count
		if count == 0:
			pl=allPlayers()
			pl = pl[start:end]
			count = 1
			p=playerdataSerializer(pl,many=True)
			context = {"status_code":200,"msg":"DataFound","players":p.data}
			return Response(context)
		global PLAYERS
		# pl=allPlayers()
		pl = PLAYERS[start:end]
		count = 1
		p=playerdataSerializer(pl,many=True)
		context = {"status_code":200,"msg":"DataFound","players":p.data}
		return Response(context)
	except:
		return Response({"status_code":400,"msg":"something went wrong"},status=400)




@api_view(["GET"])
def news(request):
	p = NEWS.objects.all().filter().order_by("-id")[:6]
	n = newsSerializer(p,many=True)
	context = {"status_code":200,"msg":"DataFound","news":n.data}
	return  Response(context)


@api_view(["GET"])
def match(request):
	fixtures = matches.objects.all().filter(matchCompleated=False).order_by("-id")[:8]
	# fixtures.insert(0,{"status_code":200})  
	fixtures = matchesSerializer(fixtures, many=True)
	context = {"status_code":200,"msg":"DataFound","fixtures":fixtures.data}
	return Response(context)




@api_view(["GET"])
def getP(request,playerId):
	try:
		pl=playerdata.objects.get(playerid=playerId)
		p=playerdataSerializer(pl,many=False)
		context = {
		"status_code":200,
		"msg":"DataFound",
		"player":p.data

		}
		return Response(context)
	except:
		context = {
		"status_code":400,
		"msg":"DataNotFound"
		}
		return Response(context)





