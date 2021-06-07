from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MyTokenObtainPairSerializer, UserSerializer




class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)