# paraphrased by https://smodin.io/zh-cn/%E8%87%AA%E5%8A%A8%E9%87%8D%E6%96%B0%E7%BC%96%E5%86%99%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E6%96%87%E6%9C%AC%E5%85%8D%E8%B4%B9
import pandas as pd
file_name = 'sampled-top-50-dev-v2.0-translated-ms-random'
df = pd.read_csv('../dataset/stanford-squad/table/{}.csv'.format(file_name), sep='\t')
with open('../dataset/stanford-squad/table/ms-converted-translation.txt', mode='r') as f:
    l = [x.strip() for x in f.readlines()]
df['question_zh-cn'] = l
df.to_csv('../dataset/stanford-squad/table/{}-paraphrased.csv'.format(file_name), sep='\t', index=False)
