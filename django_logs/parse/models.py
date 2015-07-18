from django.db import models


class Entry(models.Model):
    real_ip = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now=False)
    request = models.CharField(max_length=6)
    page = models.TextField()
    status = models.CharField(max_length=3)
    bytes_sent = models.CharField(max_length=10)
    referer = models.TextField()
    user_agent = models.TextField()
    mobile = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
