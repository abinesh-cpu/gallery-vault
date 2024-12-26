from django.db import models

# Create your models here.
class files(models.Model):
    file=models.FileField()
    description=models.CharField(max_length=30)