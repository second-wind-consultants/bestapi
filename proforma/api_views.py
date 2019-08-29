from rest_framework import viewsets
from . import models
from . import serializers

class PLAccountViewset(viewsets.ModelViewSet):
	queryset = models.PLAccount.objects.all()
	serializer_class = serializers.PLAccountSerializer