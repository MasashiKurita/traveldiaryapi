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
    diary = serializers.PrimaryKeyRelatedField()
#     diary = serializers.RelatedField(source="diary.id",)
#     diary_id = serializers.RelatedField(source="dairy.id")
    
    class Meta:
        model = MileStone
        fields = ('page_id', 'diary',)
        
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
        #return MileStone(**attrs)
        return serializers.ModelSerializer.restore_object(self, attrs, instance=instance)
    
class DiarySerializer(serializers.ModelSerializer):
    
    user_id = serializers.CharField(required=False,
                                    max_length=100)
    title = serializers.CharField(required=False,
                                  max_length=100)
    description = serializers.CharField(required=False,
                                        widget=widgets.Textarea,
                                        max_length=500)

    milestones = MileStoneSerializer(required=False,
                                     many=True,)
    
    class Meta:
        model = Diary
        fields = ('id', 'user_id', 'title', 'description', 'milestones',)
        depth = 1
                
    def validate_milestones(self, attrs, source="milestones"):
        #print("validate::diaryserializer")
        return attrs

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new diary instance, given a dictionary
        of deserialized field values.
     
        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.user_id = attrs.get('user_id', instance.user_id)
            instance.title = attrs.get('title', instance.title)
            instance.description = attrs.get('description', instance.description)
            instance.milestones = attrs.get('milestones', instance.milestones)
            return instance
     
        # Create new instance
        #return Diary(**attrs)
        return serializers.ModelSerializer.restore_object(self, attrs, instance=instance)
