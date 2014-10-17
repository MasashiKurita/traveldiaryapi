'''
Created on 2014/10/17

@author: x-masashik
'''
from django.forms import widgets
from rest_framework import serializers
from milestones.models import Diary, MileStone

class MileStoneSerializer(serializers.ModelSerializer):
    page_id = serializers.CharField(required=False,
                                    max_length=100)    
    diary = serializers.Field(source='diary.id')
    
    class Meta:
        model = MileStone
        fields = ('page_id', 'diary')

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.page_id = attrs.get('page_id', instance.page_id)
            return instance

        # Create new instance
        return MileStone(**attrs)

class DiarySerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=False,
                                    max_length=100)
    title = serializers.CharField(required=False,
                                  max_length=100)
    description = serializers.CharField(widget=widgets.Textarea,
                                 max_length=500)

    milestones = MileStoneSerializer(many=True)
    
    class Meta:
        model = Diary
        fields = ('id', 'user_id', 'title', 'description', 'milestones')

#     def restore_object(self, attrs, instance=None):
#         """
#         Create or update a new diary instance, given a dictionary
#         of deserialized field values.
#  
#         Note that if we don't define this method, then deserializing
#         data will simply return a dictionary of items.
#         """
#         if instance:
#             # Update existing instance
#             instance.user_id = attrs.get('user_id', instance.user_id)
#             instance.title = attrs.get('title', instance.title)
#             instance.description = attrs.get('description', instance.description)
#             instance.milestones = attrs.get('milestones', instance.milestones)
#             return instance
#  
#         # Create new instance
#         return Diary(**attrs)
    
