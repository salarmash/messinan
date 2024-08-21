from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Header
from .serializers import ProjectSerial, HeaderSerializer


class ProjectView(APIView):
    def get(self, request):
        project = Project.objects.all()
        data = ProjectSerial(instance=project, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class Single(APIView):
    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        data = ProjectSerial(instance=project, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class HeaderView(APIView):
    def get(self, request):
        header = Header.objects.all().last()
        data = HeaderSerializer(instance=header).data
        return Response(data=data, status=status.HTTP_200_OK)
