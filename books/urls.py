from django.urls import path

from books.views import BooksAPIView

urlpatterns = [
    path('', BooksAPIView.as_view()),
]
