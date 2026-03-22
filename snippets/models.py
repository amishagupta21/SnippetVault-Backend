from django.db import models
from languages.models import Languages
# Create your models here.

class Snippets(models.Model):
      title=models.CharField(max_length=200)
      # programming_language=models.CharField(max_length=200)
      programming_language=models.ForeignKey(Languages, on_delete=models.CASCADE,related_name="snippets")
      tags=models.CharField(max_length=200,blank=True)
      code_snippets=models.TextField()
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)

      def __str__(self):
        return self.title

      class Meta:
        verbose_name_plural = "Snippets"

      