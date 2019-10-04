from rest_framework import viewsets,permissions,mixins
from rest_framework.exceptions import APIException
from django.http import HttpResponse
from .serializers import posts_serializer,searchpost_serializer
from post.models import posts

#Get Post of User
class postsViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    

    serializer_class = posts_serializer
    
    def get_queryset(self):
        return posts.objects.filter(user=self.request.user)
        #return posts.objects.all()

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)


"""
#Get All Posts
class allpostsViewSet(viewsets.ModelViewSet):

    serializer_class = posts_serializer

    def get_queryset(self):
        return posts.objects.all()
"""

#Get All Posts
class allpostsViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):

    serializer_class = posts_serializer

    def get_queryset(self):
        return posts.objects.all()


#Search Post - Type 1(Path parameter)
class searchViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = searchpost_serializer

    def get_queryset(self):
        return posts.objects.filter(pk = self.kwargs['post_id'])


#Search Post - Type 2(url attribute parameter)
class sViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = searchpost_serializer

    def get_queryset(self):
        key = self.request.GET['id']
        return posts.objects.filter(pk = key)



"""
#Get All Posts
class allpostsViewSet(mixins.UpdateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,viewsets.GenericViewSet):

    serializer_class = posts_serializer

    def get_queryset(self):
        return posts.objects.all()
"""