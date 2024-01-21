from rest_framework import serializers

from articles.models import Article


class ArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
        ]


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'content',
        ]
