from backoffice.models import *
from rest_framework import serializers
from rest_framework import serializers
# You must import the CachedSerializerMixin and cache_registry
from rest_framework_cache.serializers import CachedSerializerMixin
from rest_framework_cache.registry import cache_registry

class CategorySerializer(CachedSerializerMixin):
    class Meta:
        model = Category
        exclude = ('createdAt',)

class AppUserSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = AppUser
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class LieuSerializer(serializers.ModelSerializer):
    refCategory = CategorySerializer(read_only=True)
    photos = PhotoSerializer(read_only=True, many=True)
    class Meta:
        model = Lieu
        fields = '__all__'


cache_registry.register(CategorySerializer)

