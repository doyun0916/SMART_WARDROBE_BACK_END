from django.conf.urls import url
from restApi import views

urlpatterns = [
    url(r'^account/reg$', views.account_register),
    url(r'^account/codesend$', views.account_codesend),
    url(r'^account/codeconfig$', views.account_codeconfig),
    url(r'^account/login$', views.account_login),
    url(r'^account/withdrawal$', views.account_withdrawal),
    url(r'^account/logout$', views.account_logout),
    url(r'^account/changepw$', views.account_changepw),
]
        
