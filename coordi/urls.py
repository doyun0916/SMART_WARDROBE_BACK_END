from django.conf.urls import url
from coordi import views

urlpatterns = [
    url(r'^coordi', views.coordination),
    url(r'^mycoordi', views.coordination_myclothes),
]

