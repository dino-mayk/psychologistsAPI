from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.models import Article
from articles.serializers import ArticlesSerializer, ArticleSerializer


class ArticlesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleApiView(APIView):
    def get_object(self, article_id):
        try:
            return Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return None

    def get(self, request, article_id, *args, **kwargs):
        article_instance = self.get_object(article_id)
        if not article_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
