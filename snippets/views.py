from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer

# class JSONResponse(HttpResponse):

    # def __init__(self, data, **kwargs):
        # content = JSONRenderer().render(data)
        # kwargs['content_type'] = 'application/json'
        # super(JSONResponse, self).__init__(content, **kwargs)

# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
    # if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        # return Response(serializer.data)
    # elif request.method == 'POST':
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def snippet_detail(request, pk, format=None):
    # try:
        # snippet = Snippet.objects.get(pk=pk)
    # except Snippet.DoesNotExist:
        # return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
        # serializer = SnippetSerializer(snippet)
        # return Response(serializer.data)
    # elif request.method == 'PUT':
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
            # return Response(serializer.data)
        # else:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'DELETE':
        # snippet.delete()
        # return HttpResponse(status=status.HTTP_204_NO_CONTENT)



# class SnippetList(APIView):

    # def get(self, request, format=None):
        # snippets = SNippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        # return Response(serializer.data)

    # def post(self, request, format=None):
        # seializer = SnippetSerializer(data=request.data)
        # if seializer.is_valid():
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):

    # def get_object(self, pk):
        # try:
            # return Snippet.objects.get(pk=pk)
        # except Snippett.DoesNotExist:
            # raise Http404

    # def get(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        # serializer = SnippetSerializer(snippet)
        # return Response(serializer.data)

    # def put(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        # snippet.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)



# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin,
        # generics.GenericAPIView):
    # queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer

    # def get(self, request, *args, **kwargs):
        # return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
        # return self.create(request, *args, **kwargs)


# class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
        # mixins.DestroyModelMixin, generics.GenericAPIView):
    # queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer

    # def get(self, request, *args, **kwargs):
        # return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
        # return self.update(request, *args, **kwargs)

    # def delete(sefl, *args, **kwargs):
        # return self.destroy(request, *args, **kwargs)


# class SnippetList(generics.ListCreateAPIView):
    # queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


# class SnippetHighlight(generics.GenericAPIView):
    # queryset = Snippet.objects.all()
    # renderer_classes = (renderers.StaticHTMLRenderer,)

    # def get(self, request, *args, **kwargs):
        # snippet = self.get_object()
        # return Response(snippet.highlighted)


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwarts):
        snippet = self.get_object()
        return Response(snippet.highlighted)

# class UserList(generics.ListAPIView):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
    # queryset = User.objects.all()
    # serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['GET'])
# def api_root(request, format=None):
    # return Response({
        # 'users': reverse('user-list', request=request, format=format),
        # 'snippets': reverse('snippet-list', request=request, format=format)
    # })
