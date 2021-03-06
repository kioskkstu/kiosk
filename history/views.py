from rest_framework import generics
from .serializers import *
from .models import *


class HistoryAPIView(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class HistoryDetailAPIView(generics.RetrieveAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

