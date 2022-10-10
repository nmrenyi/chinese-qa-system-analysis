from google.cloud import translate
import pandas as pd
from tqdm import tqdm


def main():
    file_name = './sampled-top-50-dev-v2.0'
    data_path = '{}.csv'.format(file_name)
    df = pd.read_csv(data_path, sep='\t')
    questions = df['question'].tolist()
    translation_list = []
    for question in tqdm(questions):
        translation = translate_text(question)
        translation_list.append(translation)
        print('question is: {}\n translation is: {}'.format(question, translation))
    df['question_zh-cn'] = translation_list
    df.to_csv('{}-translated.csv', sep='\t', index=False)
    print('saved!')


def translate_text(text="Hello, world!", project_id="academic-empire-365115"):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "zh-cn",
        }
    )
    for translation in response.translations:
        return translation.translated_text


if __name__ == '__main__':
    main()
