from django.db import models

# Create your models here.
class portfolio(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    subject = models.CharField(max_length = 30)
    message = models.TextField()
    
