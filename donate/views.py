from django.shortcuts import render
from .serializer import StreamerSerializer

from .models import Streamer
from rest_framework import generics, mixins, viewsets

# Create your views here.


# class StreamerAPIView(
#     generics.RetrieveUpdateDestroyAPIView,
# ):
#     serializer_class = StreamerSerializer
#     queryset = Streamer.objects.all()
#     lookup_field = "deleteKey"


# class CreateStreamerAPIView(generics.CreateAPIView):
#     serializer_class = StreamerSerializer
#     queryset = Streamer.objects.all()


class StreamerAPIViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Streamer.objects.all()
    serializer_class = StreamerSerializer
    lookup_field = "deleteKey"
    pass
