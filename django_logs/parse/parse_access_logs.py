import os
import re
from datetime import datetime


# Parses Nginx access logs in specified directory.
class Parse:
    def __init__(self, path):
        self.log_directory = os.listdir(path)
        self.logs = list()
        self.failed = list()

        for file in self.log_directory:
            with open(os.path.join(path, file), "r") as f:
                self.logs = self.logs + f.readlines()

# Create a dictionary of parses values.
    def parse(self):
        regex = re.compile(r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}) - (\S+) \[(.*)\] \"(\w{3,6}) (.*) \w{0,4}/\d\.\d\" (\d+) (\d+) "(.*)" ["](.*)["] ["]')

        for line in self.logs:
            r = regex.search(line)
            if r != None:

                entry = {
                    "real_ip": r.groups()[0],
                    "time" : datetime.strptime(r.groups()[2], "%d/%b/%Y:%H:%M:%S %z"),
                    "request": r.groups()[3],
                    "page": r.groups()[4],
                    "status": r.groups()[5],
                    "bytes_sent": r.groups()[6],
                    "referer": r.groups()[7],
                    "user_agent": r.groups()[8],
                    "mobile": True if r.groups()[8].find("Mobi") != -1 else False
                }
                yield entry
            else:
                self.failed.append(line)

# Returns access log entries that failed parsing.
    def failed_parses(self):
        return self.failed
