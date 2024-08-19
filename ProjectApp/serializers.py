from rest_framework import serializers
from .models import Category, Project, Gallery, Detail


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class ProjectSerial(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    finalImage = serializers.SerializerMethodField()
    category = CategorySerializer()
    items = DetailSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

    def get_finalImage(self, obj):
        request = self.context.get('request')
        if obj.finalImage:
            image_url = obj.finalImage.url
            return request.build_absolute_uri(image_url)
