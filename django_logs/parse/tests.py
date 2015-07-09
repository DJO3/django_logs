from django.test import TestCase
from .parse_access_logs import Parse
from .models import Entry


class ParseTestCase(TestCase):
    def test_entry_setup(self):
        path = "/Users/dave/Downloads/log"
        logs = Parse(path)
        entries = logs.parse()

        for entry in entries:
            Entry.objects.get_or_create(
                real_ip = entry["real_ip"],
                time = entry["time"],
                request = entry["request"],
                page = entry["page"],
                status = entry["status"],
                bytes_sent = entry["bytes_sent"],
                referer = entry["referer"],
                user_agent = entry["user_agent"],
                mobile = entry["mobile"]
            )
