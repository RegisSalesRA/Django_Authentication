from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from core import views
from server import settings
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token),
    path('register/', views.RegisterView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)