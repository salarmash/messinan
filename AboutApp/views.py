from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import About, Counter, Award
from .serializers import AboutSerializer, CounterSerializer, AwardSerializer


class AboutView(APIView):
    def get(self, request):
        about = About.objects.all().last()
        data = AboutSerializer(instance=about, context={"request": request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class CounterView(APIView):
    def get(self, request):
        counter = Counter.objects.all()[:4]
        data = CounterSerializer(counter, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class AwardView(APIView):
    def get(self, request):
       award = Award.objects.all().last()
       data = AwardSerializer(instance=award).data
       return Response(data=data, status=status.HTTP_200_OK)