from rest_framework import serializers
from .models import About, Gallery, Counter, Item, Award


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        exclude = ("id",)

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class AboutSerializer(serializers.ModelSerializer):
    images = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = "__all__"


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = "__all__"


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class AwardSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Award
        fields = "__all__"

