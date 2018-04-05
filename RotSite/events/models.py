from django.db import models

# Create your models here.
# Documentatation at https://docs.djangoproject.com/en/2.0/ref/models/fields/

class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    dresscode = models.CharField(max_length=100)
    event_date = models.DateField('Event date')
    def __string__(self):
        return self.title