from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.pagination import PageNumberPagination


class BlogView(APIView):
    def get(self, request):
        articles = Blog.objects.all()
        paginator = PageNumberPagination()
        posts = paginator.paginate_queryset(queryset=articles, request=request)
        data = {}
        data['posts'] = BlogSerializer(posts, many=True, context={'request': request}).data
        data['total'] = articles.count()
        data['next'] = paginator.get_next_link()
        data['previous'] = paginator.get_previous_link()
        return Response(data=data, status=status.HTTP_200_OK)


class SinglePost(APIView):
    def get(self, request, pk):
        article = Blog.objects.get(id=pk)
        data = BlogSerializer(article, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
