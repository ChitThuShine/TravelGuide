from backoffice.models import Category
from api.serializers import *
from rest_framework import generics
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from django_filters.rest_framework import DjangoFilterBackend

class CategoryListView(generics.ListCreateAPIView):
    """
            Renvoi la liste de toutes les categories disponibles
    """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering_fields = ('updatedAt', 'name')
    filter_backends = (DjangoFilterBackend,)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

