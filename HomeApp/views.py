from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hero, Partner, Testimonial, AboutOne, AboutTwo
from .serializers import HeroSerializer, PartnerSerializer, TestimonialSerializer, AboutOneSerializer, \
    AboutTwoSerializer


class HeroView(APIView):
    def get(self, request):
        hero = Hero.objects.all().last()
        data = HeroSerializer(instance=hero, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class PartnerView(APIView):
    def get(self, request):
        partner = Partner.objects.all()
        data = PartnerSerializer(instance=partner, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class TestView(APIView):
    def get(self, request):
        test = Testimonial.objects.all().last()
        data = TestimonialSerializer(instance=test, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class AboutOneView(APIView):
    def get(self, request):
        about = AboutOne.objects.all().last()
        data = AboutOneSerializer(instance=about, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class AboutTwoView(APIView):
    def get(self, request):
        about = AboutTwo.objects.all().last()
        data = AboutTwoSerializer(instance=about, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
