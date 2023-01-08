from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=5)
    subject = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
