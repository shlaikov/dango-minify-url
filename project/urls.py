from django.conf.urls import include, url

from django.contrib import admin

admin.autodiscover()

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<key>.{3})$', views.redirect, name='redirect'),
    url(r'^db', views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
