# from https://learn.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-translator?tabs=python
import requests, uuid, json
import pandas as pd
from tqdm import tqdm


def main():
    with open('../credentials/ms-translation-keys.json', mode='r') as f:
        config = json.load(f)
    # Add your key and endpoint
    key = config['key1']
    endpoint = config['text-translation']

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = config['location']

    file_name = '../dataset/stanford-squad/table/sampled-top-50-dev-v2.0'
    data_path = '{}.csv'.format(file_name)
    df = pd.read_csv(data_path, sep='\t')
    questions = df['question'].tolist()
    translation_list = []
    for question in tqdm(questions):
        translation = get_ms_translation(key, endpoint, location, question)
        translation_list.append(translation)
        print('question is: {}\n translation is: {}'.format(question, translation))
    df['question_zh-cn'] = translation_list
    df.to_csv('{}-translated-ms.csv', sep='\t', index=False)
    print('saved!')


def get_ms_translation(key, endpoint, location, text):
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
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    ans = eval(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    ans_text = ''
    for i in ans:
        print(i)
        ans_text = i['translations'][0]['text']
        break
    return ans_text


if __name__ == '__main__':
    main()
