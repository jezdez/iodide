from rest_framework import routers

from .api_views import RemoveChunkViewSet

router = routers.SimpleRouter()
router.register(r"remote_chunks", RemoveChunkViewSet, basename="remote_chunks")

urlpatterns = router.urls
