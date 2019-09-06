from django.db import models
from locations.models import Location

# Create your models here.
class PLAccount(models.Model):
	REVENUE = 'REV'
	COGS = 'COG'
	EXPENSE = 'EXP'
	PLTYPE_CHOICES = [
		(REVENUE, 'Revenue'),
		(COGS, 'Cost of Goods'),
		(EXPENSE, 'Expense'),
	]
	category 		= models.CharField(max_length=250, null=False)
	subcategory 	= models.CharField(max_length=250, null=False)
	date 			= models.DateField(null=False)
	amount			= models.DecimalField(max_digits=15, decimal_places=2, null=False)
	note			= models.TextField(blank=True, null=True)
	accountnumber 	= models.CharField(max_length=250,blank=True, null=True)
	pltype 			= models.CharField(max_length=3,choices=PLTYPE_CHOICES,default=EXPENSE,)
	location 		= models.ForeignKey('locations.Location', on_delete=models.CASCADE, default=1)

	def __str__(self):
		return self.location.name + " - " + self.category + ", " + self.date.strftime("%b %Y")