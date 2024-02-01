from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from links.models import Link
from links.serializers import LinksSerializer


class LinksAPIView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Link.objects.all()
        serializer = LinksSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
