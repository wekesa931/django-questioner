from django.conf.urls import url
from .views import (
    CreateQuestion
)


urlpatterns = [
    url(r'^questions/(?P<meetupid>\d+)/$', CreateQuestion.as_view()),
]