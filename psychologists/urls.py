from django.urls import path

from psychologists.views import PsychologistsApiView

urlpatterns = [
    path('api', PsychologistsApiView.as_view()),
]
