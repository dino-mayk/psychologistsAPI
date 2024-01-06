from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from psychologists.models import Psychologist
from psychologists.serializers import PsychologistSerializer


class PsychologistsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = Psychologist.objects.all()
        serializer = PsychologistSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
