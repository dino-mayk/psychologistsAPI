from rest_framework import viewsets

from psychologists.models import Psychologist
from psychologists.serializers import PsychologistSerializer


class PsychologistViewSet(viewsets.ModelViewSet):
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
