from django.db import models

# Create your models here.

class updates(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="updates/",null=True, blank=True)
	dis = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name



states = (
("AndhraPradesh","AndhraPradesh"),
("ArunachalPradesh","ArunachalPradesh"),
("Assam","Assam"),
("Bihar","Bihar"), 
("Chhattisgarh","Chhattisgarh"),
("Goa","Goa"),
("Gujarat","Gujarat"),
("Haryana","haryana"),
("HimachalPradesh","HimachalPradesh"),
("Jharkhand","Jharkhand"),
("Karnataka","Karnataka"),
("Kerala","Kerala"),
("MadhyaPradesh","MadhyaPradesh"),
("Maharashtra","Maharashtra"),
("Manipur","Manipur"),
("Meghalaya","Meghalaya"),
("Mizoram","Mizoram"),
("Nagaland","Nagaland"),
("Odisha","Odisha"),
("Punjab","Punjab"),
("Rajasthan","Rajasthan"),
("Sikkim","Sikkim"),
("TamilNadu","TamilNadu"),
("Telangana", "Telangana"),
("Tripura","Tripura"),
("Uttarakhand","Uttarakhand"),
("UttarPradesh","UttarPradesh"), 
("WestBengal","WestBengal"),
("AndamanAndNicobarIslands","AndamanAndNicobarIslands"),
("DaraAndNagar_HaveliAndDamanAndDiu","DaraAndNagar_HaveliAndDamanAndDiu"),
("lakshadweep","lakshadweep"),
("Delhi","Delhi"),
("ladakh","ladakh"),
("jammu_kashmir","jammu_kashmir")
)

class StateAssociations(models.Model):
	photo = models.ImageField(upload_to="StateAssociationsAll/",blank=True)
	position = models.CharField(max_length=200,blank=True)
	name=models.CharField(max_length=200,blank=True)
	state =  models.CharField(max_length=200,choices=states)
	mobile=models.CharField(max_length=100,blank=True)
	Email=models.CharField(max_length=100,blank=True)
	address=models.CharField(max_length=100,blank=True)
	# stadium=models.CharField(max_length=100,blank=True)
	# registrationNumber=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.name




class BoardManageMent(models.Model):
	name = models.CharField(max_length=100,blank=True)
	photo = models.ImageField(upload_to="BoardManageMent/",blank=True)
	position=models.CharField(max_length=100)
	AssociatedTeam=models.CharField(max_length=100)
	state=models.CharField(max_length=100,choices=states)
	# dateofbirth=models.CharField()
	def __str__(self):
		return self.name


class SelectionCommittee(models.Model):
	name = models.CharField(max_length=100,blank=True)
	photo = models.ImageField(upload_to="BoardManageMent/",blank=True)
	position=models.CharField(max_length=100)
	AssociatedTeam=models.CharField(max_length=100)
	state=models.CharField(max_length=100,choices=states)
	# dateofbirth=models.CharField()
	def __str__(self):
		return self.name


class AthletesCommission(models.Model):
	name = models.CharField(max_length=100,blank=True)
	photo = models.ImageField(upload_to="BoardManageMent/",blank=True)
	position=models.CharField(max_length=100)
	AssociatedTeam=models.CharField(max_length=100)
	state=models.CharField(max_length=100,choices=states)
	# dateofbirth=models.CharField()
	def __str__(self):
		return self.name
class matches(models.Model):
	MatchName=models.CharField(max_length=100,blank=True)
	StadiumName=models.CharField(max_length=100,blank=True)
	MatchDate = models.CharField(max_length=100,blank=True)
	team1 = models.CharField(max_length=100,blank=True)
	team2 = models.CharField(max_length=100,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return f"{self.team1} VS {self.team2}"

class allaccouncements(models.Model):
	name = models.CharField(max_length=500)
	def __str__(Self):
		return self.name

class leagues(models.Model):
	photo = models.ImageField(upload_to="leagues/")
	leagueName = models.CharField(max_length=100)
	fromStartDateToEndDate = models.CharField(max_length=100)
	aboutLeague = models.TextField()
	def __str__(self):
		return self.leagueName

