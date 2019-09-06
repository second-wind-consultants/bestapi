from rest_framework import serializers
from . import models

class PLAccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.PLAccount
		fields = '__all__'