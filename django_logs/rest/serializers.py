from rest_framework import serializers
from parse.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('real_ip', 'time', 'request', 'page', 'status', 'bytes_sent',
                  'referer', 'user_agent', 'mobile', 'created', 'modified')
