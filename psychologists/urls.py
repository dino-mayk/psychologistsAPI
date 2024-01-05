from django.urls import include, path
from rest_framework import routers

from psychologists.views import PsychologistViewSet

router = routers.SimpleRouter()

router.register(r'psychologist', PsychologistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
