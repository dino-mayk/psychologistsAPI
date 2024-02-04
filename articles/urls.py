from django.urls import path

from articles.views import ArticleApiView, ArticlesAPIView

urlpatterns = [
    path('', ArticlesAPIView.as_view()),
    path('<int:article_id>', ArticleApiView.as_view()),
]
