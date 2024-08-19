from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Header, Service
from .serializers import HeaderSerializer, ServiceSerializer


class HeaderView(APIView):
    def get(self, request):
        header = Header.objects.all().last()
        data = HeaderSerializer(instance=header).data
        return Response(data=data, status=status.HTTP_200_OK)


class ServiceView(APIView):
    def get(self, request):
        service = Service.objects.all()
        data = ServiceSerializer(instance=service, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleService(APIView):
    def get(self, request, pk):
        service = Service.objects.get(id=pk)
        data = ServiceSerializer(instance=service, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)

