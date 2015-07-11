from django.db import models


class Entry(models.Model):
    real_ip = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=False)
    request = models.CharField(max_length=6)
    page = models.CharField(max_length=200)
    status = models.CharField(max_length=3)
    bytes_sent = models.CharField(max_length=10)
    referer = models.CharField(max_length=200)
    user_agent = models.CharField(max_length=200)
    mobile = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
