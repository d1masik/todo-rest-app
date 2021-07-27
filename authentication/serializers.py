from abc import ABC

from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['email'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            **kwargs
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if not password == password2:
            raise serializers.ValidationError({'password': 'Password mismatch'})
        user.set_password(password)
        user.save()
        return user


class IpUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'ipaddress']
