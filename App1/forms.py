from App1.models import TODOLIST, Users
from django.forms import ModelForm

class ToDoForm(ModelForm):
	class Meta:
		model = TODOLIST
		fields = ['title', 'content']

class UsersForm(ModelForm):
	class Meta:
		model = Users
		fields = ['username', 'email', 'DOB']