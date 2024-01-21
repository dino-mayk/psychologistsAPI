from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from psychologists.models import Psychologist
from psychologists.serializers import PsychologistSerializer


class PsychologistsApiView(APIView):
    def get(self, request, *args, **kwargs):
        psychologists = Psychologist.objects.all()
        serializer = PsychologistSerializer(psychologists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
