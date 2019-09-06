from rest_framework import viewsets
from . import models
from . import serializers

class LocationViewset(viewsets.ModelViewSet):
	queryset = models.Location.objects.all()
	serializer_class = serializers.LocationSerializer