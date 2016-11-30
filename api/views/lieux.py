from backoffice.models import Lieu
from api.serializers import *
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework import generics
import django_filters

class LieuFilter(django_filters.rest_framework.FilterSet):
    categoryName = django_filters.CharFilter(name="refCategory__name",lookup_expr='contains')
    class Meta:
        model = Lieu
        fields = ['refCategory','categoryName']


class LieuListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Lieu.objects.all().select_related('refCategory').prefetch_related('photos')
    serializer_class = LieuSerializer
    filter_class = LieuFilter
    distance_filter_field = 'location'
    ordering = ('location',)
    distance_filter_convert_meters = True
    bbox_filter_include_overlapping = False  # Optional

    def get_queryset(self):
        queryset = Lieu.objects.filter(valide=True).select_related('refCategory').prefetch_related('photos')
        return queryset


class LieuDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Lieu.objects.all().select_related('refCategory').prefetch_related('photos')
    serializer_class = LieuSerializer

