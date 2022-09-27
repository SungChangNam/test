from re import M
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models

# Create your models here.
class AccessLog(models.Model):
    create_at = models.DateTimeField("접속 시간", auto_now_add=True)
    locations = models.CharField("접속 경로",max_length=50)
    
    def __str__(self):
        return f"{self.create_at}/ {self.locations} "