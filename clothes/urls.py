from django.conf.urls import url
from clothes import views

urlpatterns = [
    url(r'^clothes/insert', views.item_insert),
    url(r'^clothes/get', views.item_get),
    url(r'^clothes/update', views.item_update),
    url(r'^clothes/delete', views.item_update)
]

