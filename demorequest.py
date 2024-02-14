import requests

# payload = {
#     'pages': 2,
#     'count': 25,
# }
# req = requests.get('https://httpbin.org/get', params=payload)

payload = { # pass the params to the form
    'username': 'ZaidArman',
    'password': 'test',
}
req = requests.post('https://httpbin.org/post', data=payload)
r_dict = req.json() # convert json into dict
print(r_dict['form'])