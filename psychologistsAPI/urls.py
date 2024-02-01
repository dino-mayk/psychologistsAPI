from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('psychologists/', include("psychologists.urls")),
    path('timetable/', include("timetable.urls")),
    path('articles/', include("articles.urls")),
    path('links/', include("links.urls")),
    path('books/', include("books.urls")),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
