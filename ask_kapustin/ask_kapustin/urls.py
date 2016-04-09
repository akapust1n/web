from django.conf.urls import patterns, include, url

from django.contrib import admin
from ask_kapustin_app import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.get_post_params, name="test")
] 
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

