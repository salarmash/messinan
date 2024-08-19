from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerial


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
