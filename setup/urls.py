from rest_framework import routers
from setup.views import ToDoViewSet

router = routers.DefaultRouter()
router.register(r'api', ToDoViewSet)

urlpatterns = router.urls


