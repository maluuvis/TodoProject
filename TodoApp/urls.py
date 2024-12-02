from django.urls import path #path define as URLs
from . import views #impota o arquivo views

urlpatterns = [ #lista
    path('', views.index, name='todo-index'), #''=url acessada, views.index=função index de views.py, name=nomeia a url
    path('update/<int:pk>', views.update, name='todo-update'),
    path('boatarde/', views.view_boatarde, name='boa-tarde'),
    path('delete/<int:pk>', views.delete, name='todo-delete'),

]