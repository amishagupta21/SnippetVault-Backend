from django.db import models

# Create your models here.
class Tags(models.Model):
      tag_name=models.CharField(max_length=200)
      tag_color=models.CharField(max_length=50)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.tag_name
      
      class Meta:
        verbose_name_plural = "tags"