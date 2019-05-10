from django.db import models
from authentication.models import Meetup

# Create your models here.
class Questions(models.Model):
    qtitle = models.CharField(max_length=255)
    qdetail = models.CharField(max_length=255, unique=True)
    qvotes = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    mtp_id = models.ForeignKey(Meetup, on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.qtitle)