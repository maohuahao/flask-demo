import requests
import json

payload = {
    'username': 'admin',
    'password': '123456',
    'provider': 'db'
}
# get access_token
base_url = 'http://192.168.56.101:8088/'
r = requests.post(base_url + '/api/v1/security/login', json=payload)
access_token = r.json()
print(access_token)
headersAuth = {
    'Authorization': 'Bearer ' + access_token['access_token']
}
# get info of dashboard
resp_info = requests.get(base_url + '/api/v1/dashboard/_info', headers=
headersAuth)
resp_dashboard = resp_info.json()
print(resp_dashboard)

# get list of dashboard
q = {'keys': ['result']}
r3 = requests.get(base_url + '/api/v1/dashboard/', headers=headersAuth)
resp_dashboard = r3.json()

# print(json.dumps(resp_dashboard))
for result in resp_dashboard['result']:
    print(result['dashboard_title'], result['id'])

# key = resp_dashboard['result'][0].keys()
# print(key)
# get list of charts
r2 = requests.get(base_url + '/api/v1/chart/', headers=headersAuth)
resp_chart = r2.json()
print(json.dumps(resp_chart))
for result in resp_chart['result']:
    print(result['slice_name'], result['id'])

exportchart = requests.get(base_url + '/api/v1/chart/export/', headers=headersAuth)
resp_chart = exportchart.json()
print(resp_chart)

# 获取如我们已经开发过dashboard list
dlists = requests.get(base_url + '/api/v1/dashboard/', headers=headersAuth)
resp_dashboard = dlists.json()
for result in resp_dashboard['result']:
    print(result['dashboard_title'], result['id'])

# 获取已经创建的Charts
chartLists = requests.get(base_url + '/api/v1/chart/', headers=headersAuth)
resp_chart = chartLists.json()
for result in resp_chart['result']:
    print(result['slice_name'], result['id'])
