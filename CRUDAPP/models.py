from django.db import models

# Create your models here.
class StudentData(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

