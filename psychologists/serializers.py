from rest_framework import serializers

from psychologists.models import Psychologist


class PsychologistSerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    patronymic = serializers.CharField(max_length=50)
    photo = serializers.ImageField()

    def create(self, validated_data):
        psychologist = Psychologist.objects.create(**validated_data)
        return psychologist

    class Meta:
        model = Psychologist
        fields = [
            'id',
            'name',
            'surname',
            'patronymic',
            'photo',
        ]
