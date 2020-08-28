import urllib.request
import urllib.parse
import json

url = "https://gitlab.com/api/v4/runners"
payload = {"description": "python_register_runner_1",
           "tag_list": "python, urllib_request", "token": "<GITLAB_RUNNER_TOKEN>"}
           
data = urllib.parse.urlencode(payload)
data = data.encode('ascii')

with urllib.request.urlopen(url=url, data=data) as f:
    res = f.read().decode('utf-8')
    print(res)

resjson = json.loads(res)
print(resjson['token'])
# output
# {"id":2740102,"token":"3yjprvXXXXXX-whTweGAp"}
# <runner token>
# 3yjprvXXXXXX-whTweGAp
