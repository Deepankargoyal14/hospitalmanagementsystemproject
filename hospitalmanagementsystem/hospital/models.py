from django.db import models

# Create your models here.
class Patient(models.Model):
	Patient_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=20)
	phonenumber = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=20)

	def __str__(self):
		return self.Patient_name

class LoginTable(models.Model):
	csrfmiddlewaretoken = models.TextField(null=True)
	email = models.EmailField(unique=True)

	def __str__(self):
		return self.email