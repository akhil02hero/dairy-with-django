from django.db import models
from datetime import datetime
# Create your models here.
class data(models.Model):
    date=models.DateField(auto_now_add=True)
    title=models.CharField(max_length=200)
    story=models.TextField()
