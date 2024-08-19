from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Info, Form
from .serializers import InfoSerializer, FormSerializer


class ContactView(APIView):
    def get(self, request):
        info = Info.objects.all()
        data = InfoSerializer(instance=info, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "message": "درخواست با موفقیت ثبت شد",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "status": 400,
            "message": "مشکلی پیش آمده",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
