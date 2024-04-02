from rest_framework import serializers

from memory.models import Memory, Post, Picture


class MemorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Memory
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Post
        fields='__all__'


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model=Picture
        fields='__all__'
