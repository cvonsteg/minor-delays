import requests
import json

class TFL:
    def __init__(self, lines):
        self.lines = lines
        self.request = None
        # Populate request
        self._send_api_request()

    def _send_api_request(self):
        self.request = requests.get('https://api.tfl.gov.uk/line/mode/tube/status').json()

    def tube_status(self, wanted_line):
        for i in range(len(self.request)):
           line_wanted = self.request[i]['name']
           if line_wanted.upper() == wanted_line.upper():
               return (line_wanted, self.request[i]['lineStatuses'][0]['statusSeverityDescription'])

    def status_dict(self):
        return {self.tube_status(i)[0]: self.tube_status(i)[1] for i in self.lines}

    def print_status(self):
        statuses = self.status_dict()
        for k, v in statuses.items():
            print(f'\nLine: {k}\nStatus: {v}\n')


if __name__ == "__main__":
    pass
