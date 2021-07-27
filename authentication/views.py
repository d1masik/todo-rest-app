from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.models import User
from authentication.serializers import RegistrationSerializer, IpUserSerializer
from authentication.utils import get_user_ip


class RegisterView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, ipaddress=get_user_ip(request))
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, **kwargs):
        serializer.save(**kwargs)


class IpUsersListView(ListAPIView):
    serializer_class = IpUserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(ipaddress=get_user_ip(request)))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, **kwargs):
        return self.queryset.filter(**kwargs)
