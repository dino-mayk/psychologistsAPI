from django.urls import path

from psychologists.views import PsychologistsApiView

urlpatterns = [
    path('', PsychologistsApiView.as_view()),
]
