from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('getalluser/',views.getalluser),
   path('getuser/<int:id>/',views.getuser),
   path('saveuser/',views.saveuser),
   path('updateuser/<int:id>/',views.updateuser),
   path('deleteuser/<int:id>/',views.deleteuser),
]