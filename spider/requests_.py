# sudo pip3 install requests

import requests

# different kinds of requests
r = requests.get('https://api.github.com/events')
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

# params
payload = {'key1': 'value1', 'key2': 'value2'}
r1 = requests.get('https://httpbin.org/get', params=payload)

payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r2 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r3 = requests.post('https://httpbin.org/post', data=payload_dict)

payload_json = {'some': 'data'}
r4 = requests.post('https://api.github.com/some/endpoint', json=payload_json)

# headers
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get('https://api.github.com/some/endpoint', headers=headers)

# cookies
cookies = dict(cookies_are='working')
r = requests.get('https://httpbin.org/cookies', cookies=cookies)

# upload file
files = {'file': open('report.xls', 'rb')}
r = requests.post('https://httpbin.org/post', files=files)

# timeout
requests.get('https://github.com/', timeout=0.001)

# response
r.text
r.status_code
r.content
r.encoding
r.headers
r.json
r.cookies['example_cookie_name']

# stream
r = requests.get('https://api.github.com/events', stream=True)
r.raw
r.raw.read(10)
