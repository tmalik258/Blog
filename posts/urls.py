from django.urls import path

from rest_framework.routers import SimpleRouter

from accounts.views import UserViewSet
from posts.views import PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls