from django.conf.urls import url
from coordi import views

urlpatterns = [
    url(r'^coordi', views.coordination),
    url(r'^mycoordi', views.coordination_myclothes),
    url(r'^likecoordi', views.coordination_like),
    url(r'^infolikecoordi', views.coordination_get_like),
    url(r'^allmycoordi', views.func_temp),
]

