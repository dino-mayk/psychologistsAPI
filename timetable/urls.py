from django.urls import path

from timetable.views import (RecruitingTimetableApiView, TimetableApiView,
                             TimetableDetailApiView)

urlpatterns = [
    path('api', TimetableApiView.as_view()),
    path('recruiting/api', RecruitingTimetableApiView.as_view()),
    path('<int:timetable_id>/api', TimetableDetailApiView.as_view()),
]
