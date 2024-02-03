from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactAPIView(APIView):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
