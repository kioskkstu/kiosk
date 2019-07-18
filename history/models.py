from django.db import models


class History(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name')
    text = models.TextField(verbose_name='Text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
