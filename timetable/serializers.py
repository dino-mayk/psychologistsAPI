from rest_framework import serializers

from timetable.models import Timetable


class TimetableSerializer(serializers.ModelSerializer):
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


class TimetableDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = [
            'id',
            'theme',
            'photo',
            'content',
        ]
