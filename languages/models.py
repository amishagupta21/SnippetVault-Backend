from django.db import models

# Create your models here.

class Languages(models.Model):
       language_name=models.CharField(max_length=200)
       syntax_identifier=models.CharField(max_length=200, unique=True)
       language_icon=models.CharField(max_length=200)
       description=models.TextField(blank=True)
       created_at=models.DateTimeField(auto_now_add=True)
       updated_at=models.DateTimeField(auto_now=True)

       def __str__(self):
              return self.language_name
