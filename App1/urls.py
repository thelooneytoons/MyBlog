from django.urls import path
from App1 import views



urlpatterns = [
    path('', views.Home, name= 'App1-Todo'),
    path('Functional/', views.ToDoApp.as_view(), name= 'App1-Functional'),
    path('detail-view/?<int:pk>/', views.detail_view, name= 'detail-view'),
    path('edit/?<int:pk>/', views.edit, name= 'edit'),
    path('save/?<int:pk>/', views.save, name= 'save'),
    path('delete/?<int:pk>/', views.delete, name= 'delete'),
    path('register/', views.register, name= 'register'),
    ]