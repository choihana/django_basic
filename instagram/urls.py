from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets
from . import views
router = DefaultRouter()
router.register('post', viewsets.PostViewSet, basename='post') #2개의 url 생성
router.register('public', viewsets.PublicPostViewSet, basename='post2')


urlpatterns=[
    #path('', views.post_list, name='post_list'),
    #path('public/', views.PostListAPIView.as_view()),
    *router.urls,
]