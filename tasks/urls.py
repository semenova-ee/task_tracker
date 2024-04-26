from rest_framework import routers
from .views import TaskViewSet

router = routers.SimpleRouter()
router.register(r"", TaskViewSet)

urlpatterns = []

urlpatterns += router.urls
