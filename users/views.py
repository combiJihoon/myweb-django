from .serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model

User = get_user_model()


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
