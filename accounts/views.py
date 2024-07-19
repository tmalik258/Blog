from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from accounts.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser,]
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
