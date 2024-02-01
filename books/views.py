from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BooksSerializer


class BooksAPIView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Book.objects.all()
        serializer = BooksSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
