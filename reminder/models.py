from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField()        
    date = models.DateField()                 
    time = models.TimeField()                
    category = models.CharField(max_length=100)  

    def __str__(self):
        return self.title  
