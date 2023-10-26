from api_tests import Request
import sys


def parse_request_amount() -> int | None:
    if __name__ != '__main__':
        return None
    args = sys.argv
    if len(args) != 2:
        return None
    try:
        return int(args[1])
    except ValueError:
        return None


HOST = 'localhost'
PORT = 80
req = Request(HOST, PORT)

filename = 'api_tests/test.jpg'
req.load_image(filename)
url = '/v1/extract'
headers = {
    'Content-Type': 'image/jpeg',
    'X-Request-ID': '4896c91b-9e61-3129-87b6-8aa299028058'
}
request_count = parse_request_amount()
if not request_count:
    request_count = 5

requests_time = req.get_request_time_sync(url, headers, request_count)

print(f'\nNumber of requests: {request_count}\n'
      f'Average server response time: {(requests_time / request_count):.3f} ms.')
