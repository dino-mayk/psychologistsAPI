from django.urls import path

from links.views import LinksAPIView

urlpatterns = [
    path('api', LinksAPIView.as_view()),
]
