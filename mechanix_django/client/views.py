from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ClientSerializer,RegisterSerializer
from .models import Client

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny


from django.core.exceptions import PermissionDenied
 

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner!')
        serializer.save()




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer