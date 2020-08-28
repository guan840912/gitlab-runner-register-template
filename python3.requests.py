import json
import requests

url = "https://gitlab.com/api/v4/runners"

# for python # for python requests
requestspayload = dict(description="python_register_runner_2",
                       tag_list="python, requests", token="<GITLAB_RUNNER_TOKEN>")

req = requests.post(data=requestspayload, url=url)
jsonres = json.loads(req.content.decode('utf-8'))

print(jsonres)
print(jsonres['token'])

# output
# {"id":2740102,"token":"3yjprvXXXXXX-whTweGAp"}
# <runner token>
# "3yjprvXXXXXX-whTweGAp
