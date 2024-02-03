from django.db import models


class Contact(models.Model):
    TYPES = [
        (1, 'Телефон'),
        (2, 'Электронная почта'),
        (3, 'Адресс'),
    ]
    type = models.PositiveSmallIntegerField(
        choices=TYPES,
    )
    data = models.CharField(max_length=250)

    def __str__(self):
        return self.data
