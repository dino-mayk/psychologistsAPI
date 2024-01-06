from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from timetable.models import Timetable
from timetable.serializers import TimetableSerializer


class TimetableApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = Timetable.objects.all()
        serializer = TimetableSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
