from django.db import models


class Link(models.Model):
    domain = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.domain

    class Meta:
        ordering = ['created_on']
