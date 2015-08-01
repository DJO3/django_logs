from django.conf.urls import url
from parse import views

urlpatterns = [
    url(r'^$', views.ParseIndex.as_view(), name="index"),
]
