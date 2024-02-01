from django.urls import path

from books.views import BooksAPIView

urlpatterns = [
    path('api', BooksAPIView.as_view()),
]
