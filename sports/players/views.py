from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from .models import playerdata
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
#  user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')/*-
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@csrf_exempt
def home(request):
    if request.method == "POST":
        print("called Post")
        username = request.POST['u']
        password = request.POST['p']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            # return redirect("phpmailer/send_email_4_file_attachment_phpmailer.php")
            return redirect("/all")
        else:
            html = "<html><body>User Not Found.......</body></html>"
            return HttpResponse(html)
    if request.user.is_authenticated:
       
        # return redirect("phpmailer/send_email_4_file_attachment_phpmailer.php")
        return redirect("/all")

        
    return render(request,"login/login.html")


def signup(request):
    if request.method == "GET":
        username = request.GET['username']
        password = request.GET['password']
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        return render(request,"home.html")




@login_required
def upload(re):
    x = User.objects.get(id = re.id)
    if x.isplayer == False and  re.method == "POST":
        u = User.objects.get(id = re.user.id)
        obj = playerdata()
        obj.firstname = re.POST["firstname"]
        obj.lastname = re.POST["lastname"]
        obj.fathername =  re.POST["fathername"]
        obj.address = re.POST["address"]
        obj.phonenumber = re.POST["phone"]
        obj.Email = re.POST["email"]
        obj.gender = re.POST["gender"]
        obj.city = re.POST["city"]
        obj.state = re.POST["choose_your_state"]
        obj.photo = re.FILES.get("ph")
        print("filed", re.POST.get("ph"))
        # print(re.POST["profile"])
        # print("photo")
        obj.adhar = re.FILES.get("adhar")
        obj.birth=re.FILES.get("bi")
        obj.team = u
        obj.save()
        # hfi
        print(obj.id)
        obj.playerid = f"HFI{obj.id}"
        obj.save()
        user = User.objects.create_user(username = "obj.playerid",password= re.POST["phone"] ,isplayer=True )
        return render(re,"id/index.html",{"d":obj})
    return render(re,"index.html")
    

@login_required

def log(request):
    logout(request)
    return redirect('/') 

@login_required

def search(req):
    if req.method =="POST":
        data = req.POST["player"]
        d = playerdata.objects.get(playerid = data)
        print(d)

        return render(req,"dashboard.html",{"data":d})






def  genarateIdcard(req):
    if req.method == "POST":
        data = req.POST["playerid"]
        id  = playerdata.objects.get(playerid = data)
        return render(req,"idcard/index.html",{"d":id})




@login_required
def all(request):
    x = User.objects.get(id = request.user.id)
    if request.user.is_superuser: 
        data = playerdata.objects.all()
        return render(request,"admin/admin_panel.html",{"data":data,"x":True})
    if x.isplayer :
        data  =  playerdata.objects.all().filter(playerid = request.user)
        return render(request,"admin/admin_panel.html",{"data":data,"x":False})
    data  =  playerdata.objects.all().filter(team = User.objects.get(id = request.user.id))
    return render(request,"admin/admin_panel.html",{"data":data,"x":True})
  




def rege(re):
    if re.user.isplayer == False and  re.method == "POST":
        u = User.objects.get(id = re.user.id)
        obj = playerdata()
        obj.firstname = re.POST["firstname"]
        obj.lastname = re.POST["lastname"]
        obj.fathername =  re.POST["fathername"]
        obj.address = re.POST["address"]
        obj.phonenumber = re.POST["phone"]
        obj.Email = re.POST["email"]
        obj.gender = re.POST["gender"]
        obj.city = re.POST["city"]
        obj.state = re.POST["choose_your_state"]
        obj.photo = re.FILES.get("ph")
        obj.adhar = re.FILES.get("adhar")
        obj.birth=re.FILES.get("bi")
        obj.team = u
        obj.save()
        print(obj.id)
        obj.playerid = f"HFI{obj.id}"
        obj.save()
        user = User.objects.create_user(username = obj.playerid,password= re.POST["phone"] ,isplayer=True )
        return render(re,"idcard/index.html",{"d":obj})
    if re.user.isplayer :
        return HttpResponse("<center><h1>u dont have permission to access this form</h1><h1>bye bye</h1></center>")
    return render(re,"index.html")




def getid(request):
    x = request.GET['idd']
    obj = playerdata.objects.get(playerid=x)
    return render(request,"idcard/index.html",{"d":obj})
