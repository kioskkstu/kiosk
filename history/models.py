from django.db import models


class History(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()
