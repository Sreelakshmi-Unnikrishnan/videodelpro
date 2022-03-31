from django.db import models
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField()
    active = models.BooleanField( default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
           return "ID: " + str(self.id) + " | Video: " + str(self.title)
