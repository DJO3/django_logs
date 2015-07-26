from django.core.management.base import BaseCommand
from parse.management.parse_access_logs import Parse
from parse.models import Entry


# Inserts access logs as Entries. Uses first argument as log directory.
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('log_dir', nargs='+', type=str)

    def handle(self, *args, **options):
        log_dir = options['log_dir'][0]
        logs = Parse(log_dir)
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
