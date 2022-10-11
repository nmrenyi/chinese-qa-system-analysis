import json
from tqdm import tqdm
import importlib  
import pandas as pd

def main():
    with open('../credentials/ms-translation-keys.json', mode='r') as f:
        config = json.load(f)
    # Add your key and endpoint
    key = config['key1']
    endpoint = config['text-translation']

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = config['location']

    file_name = '../dataset/labelling/pre-labelled'
    data_path = '{}.tsv'.format(file_name)
    df = pd.read_csv(data_path, sep='\t')
    candidates = df['answer_text'].tolist()
    translation_list = []

    get_ms_translation = importlib.import_module("ms-translation").get_ms_translation

    for question in tqdm(candidates):
        translation = get_ms_translation(key, endpoint, location, question)
        translation_list.append(translation)
        print('question is: {}\n translation is: {}'.format(question, translation))
    df['answer_text_zh-cn'] = translation_list
    df = df[['question_index', 'translation_engine', 'question_type', 'question',
       'question_zh-cn', 'answer_text', 'answer_text_zh-cn', 'baidu', 'baidu_acc', 'yuan1.0',
       'yuan1.0_acc', 'zhiyuan', 'zhiyuan_acc', 'answer_start',
       'answer_context', 'question_id', 'title']]
    df.to_csv('{}-translated-ms.tsv'.format(file_name), sep='\t', index=False)
    print('saved!')


if __name__ == '__main__':
    main()
