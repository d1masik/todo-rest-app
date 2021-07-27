from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from todo.models import Card
from todo.serializers import CreateTodoSerializer, AllTodoSerializer, UpdateTodoSerializer


class TodoViewSet(ModelViewSet):
    serializer_class = AllTodoSerializer
    queryset = Card.objects.all()

    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = CreateTodoSerializer
        if self.action == 'update':
            self.serializer_class = UpdateTodoSerializer
        return self.serializer_class

    def get_queryset(self):
        user = self.request.user
        return Card.objects.filter(user=user)

    def perform_create(self, serializer, **kwargs):
        return serializer.save(**kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def done(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(done=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
