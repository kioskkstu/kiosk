from django.db import models


class History(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
