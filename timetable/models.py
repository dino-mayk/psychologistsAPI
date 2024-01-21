from django.db import models


class Timetable(models.Model):
    date = models.CharField(max_length=250)
    timeStart = models.TimeField()
    timeEnd = models.TimeField()
    theme = models.CharField(max_length=250)
    presenter = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.presenter} {self.theme}'

    class Meta:
        ordering = ['created_on']
