from django.conf.urls import url
from HeartsMainApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
