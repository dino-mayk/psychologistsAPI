from django.urls import path

from links.views import LinksAPIView

urlpatterns = [
    path('', LinksAPIView.as_view()),
]
