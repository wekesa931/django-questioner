from rest_framework import serializers
from .models import Meetup

class MeetupSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Meetup
        fields = (
            'id','name','likes','date_created','date_modified'
        )
        read_only_fields = (
            'date_created','date_modified'
        )