from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from checks.models import Check
from checks.serializers import CheckSerializer
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer

    def get_queryset(self):
        # Only allow a user to see their own checks
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically link the new check to the logged-in user
        serializer.save(user=self.request.user)