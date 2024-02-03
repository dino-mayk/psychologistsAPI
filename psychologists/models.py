from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Psychologist(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    patronymic = models.CharField(max_length=250)
    photo = models.ImageField(
        upload_to='uploads/photos/psychologists/%Y/%m',
        null=True,
    )
    position = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    description = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)

    @property
    def get_photo(self):
        return get_thumbnail(
            self.photo,
            '300x300',
            crop='center',
            quality=51,
        )

    def img_tmb(self):
        if self.photo:
            return mark_safe(
                f'<img src="{self.get_photo.url}">'
            )
        return 'no photo'

    img_tmb.short_description = 'photo'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        ordering = ['created_on']
