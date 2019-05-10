from django.shortcuts import render
from rest_framework import generics
from .models import Questions
from .serializers import QuestionSerializer
from authentication.models import Meetup

# Create your views here.
class CreateQuestion(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        meetup = Meetup.objects.get(id=self.kwargs['meetupid'])
        mtp_detail = {
            'name':meetup.name,
            'id':meetup.id
        }
        serializer.save(mtp_id=meetup)
        # prin
        # return {'serializer.data': 'ghhhghg'}
        

    
