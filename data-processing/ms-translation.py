# from https://learn.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-translator?tabs=python
import requests, uuid, json

with open('../credentials/ms-translation-keys.json', mode='r') as f:
    config = json.load(f)


# Add your key and endpoint
key = config['key1']
endpoint = config['text-translation']

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = config['location']

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['zh-Hans']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'I would really like to drive your car around the block a few times!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

ans = eval(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

ans_text = ''
for i in ans:
    print(i)
    ans_text = i['translations'][0]['text']
    break
print(ans_text, type(ans_text))
