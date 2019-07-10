from rest_framework import serializers

from .models import *


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('name', 'text', )