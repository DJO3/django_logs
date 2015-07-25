import os
import re
import sys
from datetime import datetime
from shutil import move


# Parses Nginx access logs in specified directory.
class Parse:
    def __init__(self, path):
        self.log_files = os.listdir(path)
        self.logs = list()
        self.failed = list()

        # Verify processed directory exists to store log files for parsing.
        parent_dir = os.path.abspath(os.path.join(path, os.pardir))
        processed_dir = os.path.join(parent_dir, "processed")
        if not os.path.exists(processed_dir):
            os.makedirs(processed_dir)

        # Moves each file to a processed directory and then reads contents.
        for file in self.log_files:
            time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
            timestamped_file = "{0}{1}".format(time, ".log")
            log_file = os.path.join(path, file)
            if os.path.isfile(log_file) and log_file.find(".log") != -1:
                processed_file = os.path.join(processed_dir, timestamped_file)
                move(log_file, processed_file)
                with open(processed_file, "r") as f:
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

if __name__ == "__main__":
    log_dir = sys.argv[1:][0]
    logs = Parse(log_dir)
    entries = logs.parse()
    for entry in entries:
        print(entry)
