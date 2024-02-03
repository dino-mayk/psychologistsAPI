from django.urls import path

from articles.views import ArticleApiView, ArticlesAPIView

urlpatterns = [
    path('api', ArticlesAPIView.as_view()),
    path('<int:article_id>/api', ArticleApiView.as_view()),
]
