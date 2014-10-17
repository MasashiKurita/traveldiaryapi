from django.shortcuts import render
from rest_framework import viewsets
from milestones.models import Diary, MileStone
from milestones.serializers import DiarySerializer, MileStoneSerializer

# Create your views here.

class DiaryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

class MileStoneViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MileStone.objects.all()
    serializer_class = MileStoneSerializer