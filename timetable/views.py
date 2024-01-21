from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from timetable.models import Timetable
from timetable.serializers import TimetableSerializer


class TimetableApiView(APIView):
    def get(self, request, *args, **kwargs):
        timetable = Timetable.objects.all()
        serializer = TimetableSerializer(timetable, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
