from backoffice.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
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


