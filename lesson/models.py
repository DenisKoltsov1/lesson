from django.db import models
from django.urls import reverse



class Lesson(models.Model):
    
    name = models.CharField(max_length=255)
    link= models.CharField(max_length=255)
    duration=models.IntegerField()

    def __str__(self):
        return self.name, self.link 


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name_plural = 'Урок'