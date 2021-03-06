from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

    
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'email',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email',)
