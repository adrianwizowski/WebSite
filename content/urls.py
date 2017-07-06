from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^en/', views.base, name='base'),
    url(r'^pl/', views.base_pl, name='base_pl'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

