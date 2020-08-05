from django.db import models

class Blog(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateField()

