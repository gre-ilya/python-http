from api_tests import Request

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
request_count = 100

requests_time = req.get_request_time_sync(url, headers, request_count)


print(f'Number of requests: {request_count}\n'
      f'Average server response time: {requests_time / request_count} sec.')
