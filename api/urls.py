from rest_framework import routers
from .api import ApiViewsets

router = routers.DefaultRouter()

router.register('app/api', ApiViewsets, 'app')

urlpatterns = router.urls
