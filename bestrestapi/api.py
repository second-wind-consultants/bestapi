from rest_framework import routers
from proforma import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'placcounts',myapp_views.PLAccountViewset)