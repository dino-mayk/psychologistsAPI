from django.urls import path

from timetable.views import (RecruitingTimetableApiView, TimetableApiView,
                             TimetableDetailApiView)

urlpatterns = [
    path('', TimetableApiView.as_view()),
    path('recruiting', RecruitingTimetableApiView.as_view()),
    path('<int:timetable_id>', TimetableDetailApiView.as_view()),
]
