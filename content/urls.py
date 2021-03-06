from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.base, name='base'),
    url(r'^en/', views.base, name='base'),
    url(r'^pl/', views.base_pl, name='base_pl'),
    url(r'^donation/', views.donation, name='donation'),
    url(r'^feedback/', views.feedback, name='feedback'),
    url(r'^process/', views.paypal, name='process'),
    url(r'^done/', views.money_done, name='done'),
    url(r'^canceled/', views.money_canceled, name='canceled'),
    url(r'^air/', views.air, name='air')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

