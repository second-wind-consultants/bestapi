from rest_framework import serializers
from . import models

class PLAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.PLAccount
		fields = ('id','category','subcategory','amount','note','accountnumber','date')