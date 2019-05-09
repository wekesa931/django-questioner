from django.db import models

# Create your models here.
class Meetup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    likes = models.CharField(max_length=255, default='1')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)