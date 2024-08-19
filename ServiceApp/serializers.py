from rest_framework import serializers
from .models import Header, Service, Item


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    fullImage = serializers.SerializerMethodField()
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

    def get_fullImage(self, obj):
        request = self.context.get('request')
        if obj.fullImage:
            image_url = obj.fullImage.url
            return request.build_absolute_uri(image_url)
