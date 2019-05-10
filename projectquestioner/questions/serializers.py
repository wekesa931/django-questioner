from rest_framework import serializers
from .models import Questions
from authentication.models import Meetup

class QuestionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    meetup_name = serializers.SerializerMethodField()

    class Meta:
        model = Questions
        fields = '__all__'
        read_only_fields = (
            'date_created','date_modified','mtp_id'
        )

    @staticmethod
    def get_meetup_name(inst):
        mtp = Meetup.objects.get(questions=inst)
        print('Serializer inst ==> {}'.format(mtp.likes))
        return mtp.name