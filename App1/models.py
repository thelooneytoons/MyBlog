from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Users(User):
	"""docstring for Users"""
	DOB = models.DateField(blank= True)


class TODOLIST(models.Model):
	# author = models.ForeignKey(Users, on_delete=models.CASCADE)
	title= models.CharField(max_length=50)
	content= models.TextField()
	date= date.today()

	def __str__(self):
		return self.title