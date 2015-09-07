from django.conf.urls import url
from parse.views import ParseIndex

urlpatterns = [
    url(r'^$', ParseIndex.as_view(), name="index"),
]
