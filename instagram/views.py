from rest_framework.generics import ListAPIView
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer


# Create your views here.
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q','')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     return render(request, 'instagram/post_list.html',{
#         'post_list':qs,
#         'q':q
#     })
#

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer