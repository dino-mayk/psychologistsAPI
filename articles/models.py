from django.db import models
from tinymce.models import HTMLField


class Article(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']
