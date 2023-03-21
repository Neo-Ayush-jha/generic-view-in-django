from django.db import models

# Create your models here.
class StudentRecord(models.Model):
    name=models.CharField(max_length=152)
    email=models.EmailField()
    contact=models.IntegerField()
    city=models.CharField(max_length=120)
    def __str__(self):
        return self.name    