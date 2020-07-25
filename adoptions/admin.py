from django.contrib import admin

from .models import Pet  #To import our pet model present in the same folder

@admin.register(Pet)	 #Here we uses a python generator to register the Pet model with the admin

class PetAdmin(admin.ModelAdmin):
	list_display=['name','species','breed','age','sex']	 
	
