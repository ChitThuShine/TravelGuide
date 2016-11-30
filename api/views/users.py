from backoffice.models import AppUser
from api.serializers import *
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework import generics
import django_filters
from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from django.db import connection
import json

class AppUserFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = AppUser
        fields = ['email', 'pseudo']

class AppUserListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    filter_class = AppUserFilter


class AppUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

