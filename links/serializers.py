from rest_framework import serializers

from links.models import Link


class LinksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = [
            'id',
            'domain',
        ]
