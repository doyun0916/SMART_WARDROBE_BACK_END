from django.conf.urls import url
from clothes import views

urlpatterns = [
    url(r'^clothes/insert', views.item_insert),
    url(r'^clothes/get', views.item_get),
    url(r'^clothes/update', views.item_update),
    url(r'^clothes/del', views.item_delete),
    url(r'^clothes/allinfo', views.item_get_all),
    url(r'^clothes/like', views.item_like),
    url(r'^clothes/infolike', views.get_like),
]

