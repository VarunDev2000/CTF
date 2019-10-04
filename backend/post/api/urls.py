from rest_framework.routers import DefaultRouter
from django.urls import include, path
from post.api.views import postsViewSet,allpostsViewSet,searchViewSet,sViewSet

router = DefaultRouter()
router.register(r'listall', allpostsViewSet, basename='list_all_posts')
router.register(r'userpost', postsViewSet, basename='posts')
router.register(r'searchpost/(?P<post_id>[0-9]+)', searchViewSet, basename='searchpost1')
router.register(r'spost', sViewSet, basename='searchpost2')

urlpatterns = router.urls
