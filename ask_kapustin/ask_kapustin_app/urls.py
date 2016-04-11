from django.conf.urls import patterns, include, url

from django.contrib import admin
from ask_kapustin_app import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.get_post_params, name="test"),
    url(r'^base/', views.base, name="base"),
    url(r'^(/)?(?P<page>\d+)?$', views.index, name='/'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^question/(?P<question_id>[0-9]+)?/$', views.question, name='question'),
    url(r'^hot/', views.hot, name='hot'),
    url(r'^tag/(?P<htag>[a-zA-Z0-9]+)/(?P<page>[0-9]+)?/?$', views.tag, name='tag'),
    url(r'^', views.error, name='error'),
] 
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

