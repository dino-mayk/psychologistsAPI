from django.urls import path

from timetable.views import TimetableApiView

urlpatterns = [
    path('api', TimetableApiView.as_view()),
]
