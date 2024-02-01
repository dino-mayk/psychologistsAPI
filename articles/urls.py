from django.urls import path

from articles.views import ArticleApiView, ArticlesAPIView

urlpatterns = [
    path(
        'api',
        ArticlesAPIView.as_view(),
        name='article-list',
    ),
    path(
        'api/<int:article_id>/',
        ArticleApiView.as_view(),
        name='article-detail',
    ),
]
