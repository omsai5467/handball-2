from django.shortcuts import render
from . models import *
# Create your views here.
# from rest_framework import status
from rest_framework import status
from players.models import playerdata
from . serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

'''
sen boys = 0
jun boys = 1
sub jun boys = 2
minni boys = 3

# girls
sen women = 4
jun girls = 5
sub jun girls = 6
mini gilrs = 7

'''


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
	x = """<img src=x onerror='for(i = 10 ;i<60;i++){console.log("omsai")} '>"""
	context = {
			"status_code":200,
			"message": x,
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
		p=SinglePlayerdataSerializer(pl,many=False)
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



@api_view(["GET"])
def getBlog(request,id):
	try:
		b = blogs.objects.get(id=id)
		l = blogsSerializer(b,many=False)
		context = {
			"status_code":200,
			"msg":"DataFound",
			"blog":l.data
		}
		return Response(context)
	except:
		context = {
			"status_code":400,
			"msg":"DataNotFound",
			
		}
		return Response(context)










# views for independenceb day

@api_view(["GET"])
def playsongs(request,id):
	print(type(id))
	if id == "1":
		x = """
<iframe allow = "autoplay" width="560" height="315" src="https://www.youtube.com/embed/_xrH1N_0Xdw?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay = "true"; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>		
		"""
		context ={
			"message":x
		}
		return Response(context)
	if id == "2":
		x = """
<iframe allow = "autoplay" width="560" height="315" src="https://www.youtube.com/embed/e41Bwihtke8?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>		
		"""
		context = {
			"message":x 
		}
		return Response(context)
	if id == "3":
		x= """
<iframe allow="autoplay"  width="560" height="315" src="https://www.youtube.com/embed/wF_B_aagLfI?autoplay=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>		"""
		context={
			"message":x
		}
		return Response(context)


@api_view(["GET"])
def greet(request):
	x="""
	<img width="600px" height="300px" src="https://files.oyebesmartest.com/uploads/large/11597200584eg5.gif"/>
	Freedom is in our mind and faith is in our heart....Pride is in our soul and love for the nation in our blood....Warm wishes on Independence day.....Lets make it a cheerful day!!!!

Happy Independence day
We are happy to help you with
National Anthem
National Song
Teri mitti song
Mahatma Gandhi
Chacha Nehru
Rani Lakshmi Bai
Bhagat singh
shubhash chandra bose
jai hind
Abdul kalam<img  style= "display:none" src= x  onerror='x = document.getElementsByClassName("modal-dialog sidebar-lg sandbox-chat 400px modal-dialog-scrollable")[0].style.width="1250px"'><img  style= "display:none"  src=x onerror='x = document.getElementsByClassName("scrollbar-container user-chats h-100")[0].style.background= "url(https://i.gifer.com/origin/7a/7a6abdc338517f4cc9c983d287a7cf5a_w200.gif)"'>
	"""
	context= {
		"message":x
	}
	return Response(context)
		# x = """<img src=x onerror='for(i = 10 ;i<60;i++){console.log("omsai")} '>"""




# independece onli

@api_view(["GET"])
def freedom(request,id):
	if id == "1":
		x = """
		<img src= "https://th.bing.com/th/id/R.ba14794f4c05e693fe016f4275e2fc12?rik=MuAFJ2K1q7A8Zg&riu=http%3a%2f%2f2.bp.blogspot.com%2f-pyy5lnRW3GQ%2fUS0rZNi97_I%2fAAAAAAAABHw%2fZBDCCQBn0QQ%2fs1600%2fMahatma%2bGandhi%2bBiography.jpg&ehk=ZcU3RhqHik%2fOeED0QG%2fDWFRIRznkpp1fjZAiQl8xdi0%3d&risl=&pid=ImgRaw&r=0"/>
		Gandhi in London, 1931
Born	Mohandas Karamchand Gandhi

2 October 1869
Porbandar, Porbandar State, Kathiawar Agency, British India
(present-day Gujarat, India)
Died	30 January 1948 (aged 78)
New Delhi, Delhi, Dominion of India
(present-day India)
Cause of death	Assassination (gunshot wounds)
Monuments	

    Raj Ghat
    Gandhi Smriti

Citizenship	

    British Empire (British protected person) (1869–1947)[1]
    Dominion of India (1947–1948)

Alma mater	

    Alfred High School, Rajkot (1880 – November 1887)
    Samaldas Arts College, Bhavnagar (January 1888 – July 1888)
    Inner Temple, London (September 1888–1891)
    (Informal auditing student at University College London between 1888 and 1891)

Occupation	

    Lawyeranti-colonialistpolitical ethicist

Years active	1893–1948
Era	British Raj
Known for	

    Leadership of the campaign for India's independence from British rule
    Nonviolent resistance

Notable work
	The Story of My Experiments with Truth
Office	43rd President of the Indian National Congress
Term	1924
Predecessor	Abul Kalam Azad
Successor	Sarojini Naidu
Political party	Indian National Congress (1920–1934)[2]
Movement	Indian independence movement
Spouse(s)	Kasturba Gandhi
​
​
(m. 1883; died 1944)​
Children	

    Harilal
	Manilal
	Ramdas
	Devdas

Parents	

    Karamchand Gandhi (father)
    Putlibai Gandhi (mother)

Relatives	See Family of Mahatma Gandhi
C. Rajagopalachari (father-in-law of Gandhi's son Devdas)
Awards	Time Person of the Year (1930)[3]

		"""
		context = {
			"message":x
		}
		return Response(context)
	if id == "2":
		x= """
		<img src = "https://cdn.dollsofindia.com/images/p/people-posters/jawaharlal-nehru-GA52_l.jpg"/>
			Jawaharlal Nehru was an Indian anti-colonial nationalist, secular humanist, social democrat and author who was a central figure in India during the middle of the 20th century. Nehru was a principal leader of the Indian nationalist movement in the 1930s and 1940s. Wikipedia
Born: 14 November 1889, Prayagraj
Died: 27 May 1964, New Delhi
Spouse: Kamala Nehru (m. 1916–1936)
Organizations founded: Non-Aligned Movement, MORE
Cousins: Brijlal Nehru, Shamlal Nehru
		"""
		content = {
			"message":x
		}
		return Response(content)
	if id == "3":
		x = """
		<img src="https://i.pinimg.com/736x/7c/08/11/7c081195f508b6daffe986a3273776d3.jpg" width = 500px />
		Subhas Chandra Bose was an Indian nationalist whose defiance of British authority in India made him a hero among Indians, but his wartime alliances with Nazi Germany and Imperial Japan left a legacy vexed by authoritarianism, anti-Semitism, and military failure. Wikipedia
Born: 23 January 1897, Cuttack
Education: Scottish Church College (SCC), Presidency University, MORE
Organizations founded: Azad Hind, All India Forward Bloc, Azad Hind Radio, Indian Legion, Free India Centre
Grandchildren: Thomas Krishna, Peter Arun Pfaff, Maya Pfaff
Nephews: Sisir Kumar Bose, Amiya Nath Bose, Subrata Bose
		"""
		context = {
			"message":x
		}
		return Response(context)
	if id == "4":
		x="""
		<img src = "https://images.medindia.net/amp-images/health-images/apj-abdul-kalam.jpg" width = 700px/>
		Avul Pakir Jainulabdeen Abdul Kalam was an Indian aerospace scientist and statesman who served as the 11th President of India from 2002 to 2007. He was born and raised in Rameswaram, Tamil Nadu and studied physics and aerospace engineering. Wikipedia
Born: 15 October 1931, Rameswaram
Died: 27 July 2015, Shillong
Full name: Avul Pakir Jainulabdeen Abdul Kalam
Presidential term: 25 July 2002 – 25 July 2007
Education: Madras Institute of Technology, Anna University (1955–1957), MORE
Awards: Bharat Ratna, Veer Savarkar Award, Hoover Medal, MORE
		"""
		context = {
			"message":x
		}
		return Response(context)
	if id == "5":
		x = """
		<img src="https://media.newstrack.in/uploads/national-news//Nov/18/big_thumb/rani-laxmi-bai_61971d9490024.jpg"/>
		Lakshmibai, the Rani of Jhansi, was an Indian queen, the Maharani consort of the Maratha princely state of Jhansi from 1843 to 1853 as the wife of Maharaja Gangadhar Rao. She was one of the leading figures of the Indian Rebellion of 1857 and became a symbol of resistance to the British Raj for Indian nationalists. Wikipedia
Born: 19 November 1828, Varanasi
Died: 18 June 1858, Gwalior
Full name: Manikarnika Tambe
Spouse: Gangadhar Rao (m. 1842–1853)
Grandchild: Lakhsman Rao Jhansiwale
Children: Damodar Rao
Parents: Moropant Tambe, Bhagirathi Sapre
		"""
		context = {
			"message":x
		}
		return Response(context)
	if id == "6":
		x = """
		<img src="https://i.pinimg.com/originals/b9/ef/1b/b9ef1b5502fa92533037a3b67b4fc4e1.jpg" height=700px width=700px/>
		Bhagat Singh was a charismatic Indian revolutionary who participated in the mistaken murder of a junior British police officer in what was to be retaliation for the death of an Indian nationalist. Wikipedia
Born: 28 September 1907, Banga, Pakistan
Died: 23 March 1931, Lahore Central Jail, Lahore, Pakistan
Cremation: 23 March 1931, The National Martyrs Memorial, Machhiwara
Partner: Jaidev Kapoor
Siblings: Bibi Parkash Kaur, Ranbir Singh, Kultar Singh, Bibi Amar Kaur, Kulbir Singh, Jagat Singh, Bibi Shakuntla, Rajinder Singh
Organization founded: Naujawan Bharat Sabha
		"""
		context = {
			"message":x
		}
		return Response(context)
	if id == "7":
		x="""
		<img src="https://www.happybirthdaywishes2.com/wp-content/uploads/2021/01/republic-day-animated.gif"/>
		"""
		content = {
			"message":x
		}
		return Response(content)