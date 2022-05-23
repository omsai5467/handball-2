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
("WestBengal","WestBengal")
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
