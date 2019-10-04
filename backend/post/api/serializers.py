from rest_framework import serializers
from post.models import posts


class posts_serializer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = '__all__'

class searchpost_serializer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = ['question','description','createdAt','modifiedAt']
