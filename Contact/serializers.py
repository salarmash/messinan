from rest_framework import serializers
from .models import Info, Form


class InfoSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = "__all__"

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon:
            image_url = obj.icon.url
            return request.build_absolute_uri(image_url)


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"
