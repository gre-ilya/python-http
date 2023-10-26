from PIL import Image
import io
import http.client
from time import time


class Request:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.image_byte_array = None

    def load_image(self, filename: str) -> None:
        """
        :param str filename: path for image
        :return:
        """
        image = Image.open(filename, mode='r')
        self.image_byte_array = io.BytesIO()
        image.save(self.image_byte_array, format=image.format)
        self.image_byte_array = self.image_byte_array.getvalue()

    def send_request(self, url: str, headers: dict):
        conn = http.client.HTTPConnection('localhost', 80)
        conn.request('POST', url, headers=headers, body=self.image_byte_array)
        return conn.getresponse()

    def get_request_time(self, url: str, headers: dict, request_count: int) -> int:
        """Sends http request request_count times and returns sum of time for response waiting
        :param str url: Request url
        :param dict headers: Dict with http headers for request
        :param int request_count: Amount of requests
        :return mean sum of request waiting time for all requests:
        """
        time_sum = 0
        for i in range(request_count):
            start = int(time() * 1000)
            self.send_request(url, headers)
            stop = int(time() * 1000)
            time_sum += stop - start
        return time_sum
