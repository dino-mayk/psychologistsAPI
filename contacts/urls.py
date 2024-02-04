from django.urls import path

from contacts.views import ContactAPIView

urlpatterns = [
    path('', ContactAPIView.as_view()),
]
