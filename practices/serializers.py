from rest_framework import serializers
from .models import UserCredentials
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role
        return token


class SignupSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new user using signup form
    """

    class Meta:
        model = UserCredentials
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validate_password(validated_data['password']) is None:
            password = make_password(validated_data['password'])
            user = UserCredentials.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                password=password,
                role=validated_data['role']
            )
            return user
