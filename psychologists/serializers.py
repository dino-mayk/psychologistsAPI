from rest_framework import serializers

from psychologists.models import Psychologist


class PsychologistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Psychologist
        fields = [
            'id',
            'name',
            'surname',
            'patronymic',
            'photo',
        ]
