'''
Created on 2014/10/22

@author: x-masashik
'''
from rest_framework.compat import django_filters
from milestones.models import Diary, MileStone

class DiaryFilter(django_filters.FilterSet):
    '''
    classdocs
    '''
    user_id = django_filters.CharFilter(name='user_id')
    title = django_filters.CharFilter(name="title", lookup_type="contains")
    description = django_filters.CharFilter(name='description', lookup_type="contains")
    
    class Meta:
        model = Diary
        fields = ['title', 'description']
        
class MilestoneFilter(django_filters.FilterSet):
    '''
    classdocs
    '''
    diary = django_filters.NumberFilter(name='diary')
    page_id = django_filters.CharFilter(name='page_id')
    
    class Meta:
        model = MileStone
        fields = ['page_id', 'diary']