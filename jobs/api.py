# views

from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def blogs_api(request):
    all_stories = Blog.objects.all()
    data = BlogSerializer(all_stories, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def detail_api(request, id):
    story_detail_detail = Blog.objects.get(id=id)
    data = BlogSerializer(story_detail_detail).data
    return Response({'data': data})


class BlogListApi(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'id'
