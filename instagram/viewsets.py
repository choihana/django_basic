from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import action
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    # filter , ordering 설정
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['message']
    ordering_fields=['pk','created_at'] #ordering 허용할 리스트, 지정안하면 모든 컬럼이 ordering에 사용 가능
    ordering=['-pk'] #default ordering


    @action(detail=False, methods=['GET'])
    def public(self,request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class PublicPostViewSet(ViewSet):

    def list(self, request):
        queryset = Post.objects.filter(is_public=True)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        qs = Post.objects.get(pk=pk)
        serializer = PostSerializer(qs)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request, pk=None):
        qs = Post.objects.all()
        post = get_object_or_404(qs, pk=pk)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response({"message":"item deleted"}, status = 204)
