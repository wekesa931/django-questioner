from django.conf.urls import url
from .views import (
    CreateMeetup, GetMeetup, UpdateMeetup, DeleteMeetup
)


urlpatterns = [
    url(r'^meetups/$', CreateMeetup.as_view()),
    url(r'meetup/(?P<userid>\d+)/$', GetMeetup.as_view()),
    url(r'meetup/update/(?P<pk>\d+)/$', UpdateMeetup.as_view()),
    url(r'meetup/delete/(?P<pk>\d+)/$', DeleteMeetup.as_view()),
]
