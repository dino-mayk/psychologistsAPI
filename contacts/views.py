from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.models import Address, Email, PhoneNumber
from contacts.serializers import (AddressSerializer, EmailSerializer,
                                  PhoneNumberSerializer)


class PhoneNumbersAPIView(APIView):
    def get(self, request, *args, **kwargs):
        articles = PhoneNumber.objects.all()
        serializer = PhoneNumberSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddressesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Address.objects.all()
        serializer = AddressSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmailsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Email.objects.all()
        serializer = EmailSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
