from PIL import Image
import io
import http.client
from time import time
import json


class Request:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.image_byte_array = None
        self.res = None
        self.conn = None

    def load_image(self, filename: str) -> None:
        """
        :param str filename: path for image
        :return:
        """
        image = Image.open(filename, mode='r')
        self.image_byte_array = io.BytesIO()
        image.save(self.image_byte_array, format=image.format)
        self.image_byte_array = self.image_byte_array.getvalue()

    def send_request_sync(self, url: str, headers: dict):
        conn = http.client.HTTPConnection(self.host, self.port)
        conn.request('POST', url, headers=headers, body=self.image_byte_array)
        self.res = conn.getresponse()
        return self.res

    def get_request_time_sync(self, url: str, headers: dict, request_count: int) -> int:
        """Sends http request request_count times and returns sum of time for response waiting
        :param str url: Request url
        :param dict headers: Dict with http headers for request
        :param int request_count: Amount of requests
        :return mean sum of request waiting time for all requests:
        """
        time_sum = 0
        for i in range(request_count):
            start = int(time() * 1000)
            self.send_request_sync(url, headers)
            stop = int(time() * 1000)
            time_sum += stop - start
            print(f'[Request {i + 1:4d}] Code: {self.res.code} Worked in {stop - start} ms.')
        return time_sum

    def print_response(self) -> None:
        if not self.res:
            return

        json_string = self.res.read().decode()
        json_f = json.loads(json_string)
        for key in json_f.keys():
            print(f'{key}: {json_f[key]}')
            # if isinstance(json_f[key], list):
            #     for measure in json_f[key]:
            #         print(measure)

        # print(json.loads(tmp))
