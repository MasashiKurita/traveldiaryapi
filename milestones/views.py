from rest_framework import viewsets, filters
from milestones.models import Diary, MileStone
from milestones.serializers import DiarySerializer, MileStoneSerializer
from milestones.filters import DiaryFilter, MilestoneFilter

# Create your views here.

class DiaryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DiaryFilter
    
class MileStoneViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = MileStone.objects.all()
    serializer_class = MileStoneSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MilestoneFilter    