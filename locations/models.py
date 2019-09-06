from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Location(models.Model):
	name 			= models.CharField(max_length=250, null=False)
	state 			= models.CharField(max_length=2, null=False)
	industry		= models.CharField(max_length=250, null=False)
	subIndustry		= models.CharField(max_length=250, null=False)
	franchise 		= models.BooleanField(null=False)
	county 			= models.CharField(max_length=250, null=False)
	zipcode 		= models.CharField(max_length=5, null=False)
	newCoDate 		= models.DateField(null=True, blank=True)
	sqft 			= models.FloatField(null=True,blank=True)
	employees 		= ArrayField(base_field=models.IntegerField(),size=3,blank=True,null=True)
	openHours 		= ArrayField(base_field=models.FloatField(),size=7,blank=True,null=True)
	sfAccountId 	= models.CharField(max_length=250, null=False)

	def __str__(self):
		return self.name + ", " + self.state

