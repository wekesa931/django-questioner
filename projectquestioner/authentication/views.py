from django.shortcuts import render
from rest_framework import generics
from .serializers import MeetupSerializer
from django.core import serializers
from .models import Meetup
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class CreateMeetup(generics.ListCreateAPIView):
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer

    def perform_create(self, serializer):
        serializer.save()

class GetMeetup(generics.ListAPIView):
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer

    def get_queryset(self, *args, **kwargs):
        return Meetup.objects.filter(id=self.kwargs.get('userid'))

class UpdateMeetup(generics.UpdateAPIView):
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer

    def put(self, request, *args, **kwargs):
        """
        In case you only need to update a single part of the
        model, use partial_update instead of update
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request, pk, *args, **kwargs):
        meetup = Meetup.objects.get(pk=pk)
        meetup.likes = int(meetup.likes)+1
        meetup.save()
        
        return self.partial_update(request, *args, **kwargs)

class DeleteMeetup(generics.DestroyAPIView):
    queryset = Meetup.objects.all()
    serializer_class = MeetupSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "message": "meetup deleted"
            },
            status=status.HTTP_200_OK)
