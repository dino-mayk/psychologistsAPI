from rest_framework import serializers

from timetable.models import Timetable


class TimetableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timetable
        fields = [
            'id',
            'date',
            'timeStart',
            'timeEnd',
            'theme',
            'presenter',
            'price',
        ]
