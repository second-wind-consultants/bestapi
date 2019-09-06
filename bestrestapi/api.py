from rest_framework import routers
from proforma import api_views as pf_views
from locations import api_views as l_views

router = routers.DefaultRouter()
router.register(r'placcounts',pf_views.PLAccountViewset)
router.register(r'locations',l_views.LocationViewset)