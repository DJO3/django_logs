from django.test import TestCase
from datetime import datetime
from .parse_access_logs import Parse
from .models import Entry


class ParseTestCase(TestCase):
    def setUp(self):
        Entry.objects.create(
            real_ip="192.168.1.12",
            time=datetime.strptime("23/Jun/2015:11:10:57 +0000", "%d/%b/%Y:%H:%M:%S %z"),
            request="GET",
            page="/entry/how-create-configure-free-ssl-certificate-using-django-and-pythonanywhere",
            status="200",
            bytes_sent="5",
            referer="http://www.reddit.com/r/Python/",
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.18 Safari/537.36",
            mobile=False
        )

    def test_entry(self):
        entry = Entry.objects.get(real_ip="192.168.1.12")
        self.assertEqual(entry.real_ip, "192.168.1.12")

    def test_entry_parse_script(self):
        path = "/Users/dave/Downloads/log"
        logs = Parse(path)
        entries = logs.parse()

        for entry in entries:
            Entry.objects.get_or_create(
                real_ip=entry["real_ip"],
                time=entry["time"],
                request=entry["request"],
                page=entry["page"],
                status=entry["status"],
                bytes_sent=entry["bytes_sent"],
                referer=entry["referer"],
                user_agent=entry["user_agent"],
                mobile=entry["mobile"]
            )
