from api_tests import Request

HOST = 'localhost'
PORT = 80
req = Request(HOST, PORT)

filename = 'api_tests/test.jpg'
req.load_image(filename)
print(len(req.image_byte_array))
url = '/v1/extract'
headers = {
    'Content-Type': 'image/jpeg',
    'X-Request-ID': '4896c91b-9e61-3129-87b6-8aa299028058'
}

res = req.send_request(url, headers)

print(res.status)
print(res.msg)
