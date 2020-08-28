# This project will help you , how to register gitlab runner , not use `gitlab-runner`
## Curl
```bash
    # Register 
    curl --request POST "https://gitlab.com/api/v4/runners" \
    --form "token=<GITLAB_RUNNER_TOKEN>" \
    --form "description=curl_register_runner" \
    --form "tag_list=runner,curl"
    # output
    # {"id":2734186,"token":"q6uzKxxxxxRdzzpXXXXX"}
    # <runner token>
    # q6uzKxxxxxRdzzpXXXXX 
```

## Python 3 urllib
```python
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
```

## Python Requests
```python
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
```
