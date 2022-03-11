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
objectID = None
def getall():
    ap = playerdata.objects.all().filter(state = "andhra_pradesh(AP)").count()
    an = playerdata.objects.all().filter(state = "andaman_ut(AN)").count()
    ar = playerdata.objects.all().filter(state = "arunachalPradesh(AR)").count()
    # as = playerdata.objects.all().filter(state = "assam(AS)").count()
    # as = playerdata.objects.all().filter(state = "assam(AS)").count()
    ass = playerdata.objects.all().filter(state = "assam(AS)").count()
    br = playerdata.objects.all().filter(state = "bihar(BR)").count()
    ch = playerdata.objects.all().filter(state = "chandigarh_ut(CH)").count()
    dd = playerdata.objects.all().filter(state = "dadra(DD)").count()
    dl = playerdata.objects.all().filter(state = "delhi(DL)").count()
    ga = playerdata.objects.all().filter(state = "goa(GA)").count()
    gj = playerdata.objects.all().filter(state = "gujarat(GJ)").count()
    hr = playerdata.objects.all().filter(state = "haryana(HR)").count()
    hp = playerdata.objects.all().filter(state = "himachal(HP)").count()
    jk = playerdata.objects.all().filter(state = "jammu(JK)").count()
    jhh = playerdata.objects.all().filter(state = "jharkhand(JH)").count()
    ka = playerdata.objects.all().filter(state = "karnataka(KA)").count()
    kl = playerdata.objects.all().filter(state ="kerala(KL)").count()
    ld = playerdata.objects.all().filter(state = "lakshadweep_ut(LD)").count()
    mp = playerdata.objects.all().filter(state = "madhya(MP)").count()
    mh = playerdata.objects.all().filter(state = "maharashtra(MH)").count()
    mn = playerdata.objects.all().filter(state = "manipur(MN)").count()
    ml = playerdata.objects.all().filter(state = "meghalaya(ML)").count()
    mz = playerdata.objects.all().filter(state = "mizoram(MZ)").count()
    nl = playerdata.objects.all().filter(state = "nagaland(NL)").count()
    od = playerdata.objects.all().filter(state = "orissa(OD)").count()
    py = playerdata.objects.all().filter(state = "puducherry_ut(PY)").count()
    pb = playerdata.objects.all().filter(state = "punjab(PB)").count()
    rj = playerdata.objects.all().filter(state = "rajasthan(RJ)").count()
    sk = playerdata.objects.all().filter(state = "sikkim(SK)").count()
    tn = playerdata.objects.all().filter(state = "tamilNadu(TN)").count()
    ts = playerdata.objects.all().filter(state = "telangana(TS)").count()
    tr = playerdata.objects.all().filter(state = "tripura(TR)").count()
    up = playerdata.objects.all().filter(state = "uttar(UP)").count()
    uk = playerdata.objects.all().filter(state = "uttarakhand(UK)").count()
    wb = playerdata.objects.all().filter(state = "west_bengal(WB)").count()
    d = {
            "ap":ap,
            "an":an,
            "ar":ar,
            "as":ass,
            "br":br,
            "ch":ch,
            "dd":dd,
            "dl":dl,
            "ga":ga,
            "gj":gj,
            "hr":hr,
            "hp":hp,
            "jk":jk,
            "jh":jhh,
            "ka":ka,
            "kl":kl,
            "ld":ld,
            "mp":mp,
            "mh":mh,
            "mn":mn,
            "ml":ml,
            "mz":mz,
            "nl":nl,
            "od":od,
            "py":py,
            "pb":pb,
            "rj":rj,
            "sk":sk,
            "tn":tn,
            "ts":ts,
            "tr":tr,
            "up":up,
            "uk":uk,
            "wb":wb,


    }
    return d



@csrf_exempt
def home(request):
    if request.method == "POST":
        # print("called Post")
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
        obj.age = re.POST["age"]
        obj.state = re.POST["choose_your_state"]
        obj.photo = re.FILES.get("ph")
        # print("filed", re.POST.get("ph"))
        # print(re.POST["profile"])
        # print("photo")
        obj.adhar = re.FILES.get("adhar")
        obj.birth=re.FILES.get("bi")
        obj.team = u
        obj.save()
        # hfi
        # print(obj.id)
        playeridshortcut = re.POST["choose_your_state"]
        p = playeridshortcut[-3:-1]
        # print(p)
        # print("state")
        obj.playerid = f"HFI00{p}{obj.id}"
        obj.save()
        global objectID
        objectID = obj.playerid
        user = User.objects.create_user(username = "obj.playerid",password= re.POST["phone"] ,isplayer=True )
        # return render(re,"id/index.html",{"d":obj})
        return redirect("/geti")
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
        # print(d)

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
        z = getall()
        c = playerdata.objects.all().count()
        data = playerdata.objects.all()
        # z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35]
        return render(request,"admin/admin_panel.html",{"data":data,"x":True,"z":z,"count":c})
    if x.isplayer :
        data  =  playerdata.objects.all().filter(playerid = request.user)
        return render(request,"admin/admin_panel.html",{"data":data,"x":False})
    data  =  playerdata.objects.all().filter(team = User.objects.get(id = request.user.id))

    return render(request,"admin/admin_panel.html",{"data":data,"x":True,})









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
        obj.age = re.POST["age"]
        obj.team = u
        obj.save()
        playeridshortcut = re.POST["choose_your_state"]
        p = playeridshortcut[-3:-1]
        # print(p)
        # print("state")
        obj.playerid = f"HFI00{p}{obj.id}"
        obj.save()
        global objectID
        objectID = obj.playerid
        user = User.objects.create_user(username = obj.playerid,password= re.POST["phone"] ,isplayer=True )
        # return render(re,"idcard/index.html",{"d":obj})
        return redirect("/geti")
    if re.user.isplayer :
        return HttpResponse("<center><h1>u dont have permission to access this form</h1><h1>bye bye</h1></center>")
    return render(re,"index.html")



def geti(request):
    global objectID
    if objectID !=None:

        obj = playerdata.objects.get(playerid=objectID)
        # objectID = None
        return render(request,"idcard/index.html",{"d":obj})


def getid(request):
    x = request.GET['idd']
    obj = playerdata.objects.get(playerid=x)
    return render(request,"idcard/index.html",{"d":obj})


def delete(request):
    if request.user.is_superuser:
        obj = request.GET["idd"]
        on = playerdata.objects.get(id = obj)
        on.delete()
        return redirect("/")
