from django.db import models

# Create your models here.

class Diary(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=500, blank=True, default='')
        
    class Meta:
        ordering = ('created_time',)

class MileStone(models.Model):
    diary = models.ForeignKey(Diary, related_name="milestones")
    created_time = models.DateTimeField(auto_now_add=True)
    page_id = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created_time',)