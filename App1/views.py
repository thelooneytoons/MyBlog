from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from App1.forms import ToDoForm, UsersForm
from App1.models import TODOLIST
# Create your views here.

def Home(request):
	return render(request, 'App1/HomePage.html')

def register(request):
	form= {'register_form' : UsersForm()}
	return render(request, 'App1/register.html', form )

class ToDoApp(View):
	def get(self, request):
		form1=ToDoForm()
		context= {'forms': form1 ,
				'list': TODOLIST.objects.all().order_by('-id')
				}
		return render(request, 'App1/blog_page.html', context)

	def post(self, request):
		form1=ToDoForm(request.POST)
		if form1.is_valid():
			form1.save()
			print('hello')
			context= {'forms': ToDoForm() ,
				'list': TODOLIST.objects.all().order_by('-id')
				}
			return render(request, 'App1/blog_page.html', context )
		else:
			context= {'forms': ToDoForm() ,
						'list': TODOLIST.objects.all()}
			return render(request, 'App1/blog_page.html', context)


def detail_view(request, pk):
	task=TODOLIST.objects.get(id= pk)
	return render(request, 'App1/detail_view.html', {'task' : task})



def edit(request, pk):
	post= TODOLIST.objects.get(id= pk)
	init= {
		'content': post.content,
		'title': post.title,
	}
	edit_form= ToDoForm(request.GET or None, initial=init)
	var = {"form": edit_form, 'post': post}
	return render(request, 'App1/edit.html', var)



def save(request, pk):
	post= TODOLIST.objects.get(id= pk)
	if request.method == 'POST':
		form= ToDoForm(request.POST, instance=post)
		form.save()
		return  redirect('App1-Functional')



def delete(request, pk):
	post= TODOLIST.objects.get(id= pk)
	post.delete()
	return  redirect('App1-Functional')