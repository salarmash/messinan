from rest_framework import serializers
from .models import Hero, Partner, Testimonial, TestItems, AboutOne, AboutTwo, Counter


class HeroSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    bg_img = serializers.SerializerMethodField()

    class Meta:
        model = Hero
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

    def get_bg_img(self, obj):
        request = self.context.get('request')
        if obj.bg_img:
            image_url = obj.bg_img.url
            return request.build_absolute_uri(image_url)


class PartnerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class ItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = TestItems
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class TestimonialSerializer(serializers.ModelSerializer):
    tetsItems = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Testimonial
        fields = "__all__"


class AboutOneSerializer(serializers.ModelSerializer):
    front_img = serializers.SerializerMethodField()
    back_img = serializers.SerializerMethodField()

    class Meta:
        model = AboutOne
        fields = "__all__"

    def get_front_img(self, obj):
        request = self.context.get('request')
        if obj.front_img:
            image_url = obj.front_img.url
            return request.build_absolute_uri(image_url)

    def get_back_img(self, obj):
        request = self.context.get('request')
        if obj.back_img:
            image_url = obj.back_img.url
            return request.build_absolute_uri(image_url)


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = "__all__"


class AboutTwoSerializer(serializers.ModelSerializer):
    counter = CounterSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = AboutTwo
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
