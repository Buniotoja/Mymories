from rest_framework import viewsets, status, authentication, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Memory, Picture, Post
from .serializers import MemorySerializer, PostSerializer, PictureSerializer


class MemoryView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    @api_view(['GET'])
    def get_list(request):
        queryset=Memory.objects.all()
        serializer = MemorySerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    def get_detail(request, pk=None):
        queryset=Memory.objects.all()
        memory=get_object_or_404(queryset, pk=pk)
        serializer = MemorySerializer(memory, many=False)
        return Response(serializer.data)


class PostView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    @api_view(['GET'])
    def get_list(request, fk=None):
        queryset=Post.objects.filter(memory_id=fk)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    def get_detail(request, fk=None, pk=None):
        queryset=Post.objects.filter(memory_id=fk)
        memory=get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(memory, many=False)
        return Response(serializer.data)


class PictureView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    @api_view(['GET'])
    def get_list(request, fk=None):
        queryset=Picture.objects.filter(memory_id=fk)
        serializer = PictureSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    def get_detail(request, fk=None, pk=None):
        queryset=Picture.objects.filter(memory_id=fk)
        picture=get_object_or_404(queryset, pk=pk)
        serializer=PictureSerializer(picture, many=False)
        return Response(serializer.data)

