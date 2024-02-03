from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from timetable.models import Timetable
from timetable.serializers import (TimetableDetailSerializer,
                                   TimetableSerializer)


class TimetableApiView(APIView):
    def get(self, request, *args, **kwargs):
        timetable = Timetable.objects.all()
        serializer = TimetableSerializer(timetable, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TimetableDetailApiView(APIView):
    def get_object(self, timetable_id):
        try:
            return Timetable.objects.get(id=timetable_id)
        except Timetable.DoesNotExist:
            return None

    def get(self, request, timetable_id, *args, **kwargs):
        timetable_instance = self.get_object(timetable_id)
        if not timetable_instance:
            return Response(
                {"res": "Object with this id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TimetableDetailSerializer(timetable_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecruitingTimetableApiView(APIView):
    def get(self, request, *args, **kwargs):
        timetable = Timetable.objects.filter(recruiting=True)
        serializer = TimetableSerializer(timetable, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
