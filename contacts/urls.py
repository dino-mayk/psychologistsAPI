from django.urls import path

from contacts.views import ContactAPIView

urlpatterns = [
    path('api', ContactAPIView.as_view()),
]
