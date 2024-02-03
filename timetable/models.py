from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Timetable(models.Model):
    date = models.CharField(max_length=250)
    timeStart = models.TimeField()
    timeEnd = models.TimeField()
    theme = models.CharField(max_length=250)
    presenter = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    recruiting = models.BooleanField()
    photo = models.ImageField(
        upload_to='uploads/photos/timetable/%Y/%m',
        null=True,
    )
    content = HTMLField()
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
        return f'{self.presenter} {self.theme}'

    class Meta:
        ordering = ['created_on']
