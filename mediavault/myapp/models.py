from django.db import models

# Create your models here.

class users(models.Model):
    username=models.TextField()
    email=models.TextField()
    password=models.TextField()
    
class files(models.Model):
    file=models.FileField()
    # description=models.CharField(max_length=30)
    
class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title