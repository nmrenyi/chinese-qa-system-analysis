import argparse
import sys

import pandas as pd
from tqdm import tqdm

from baidu import read_baidu_config, baidu_ask
from zhiyuan import read_zhiyuan_config, zhiyuan_ask
from yuan1_0 import read_yuan1_0_config, yuan1_0_ask


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_file', type=str, default='../input/in1.csv', help='input file')
    parser.add_argument('--out_file', type=str, default='../output/out1.csv', help='output file')
    return parser.parse_args()


def main():
    args = parse_args()
    in_file = args.in_file
    out_file = args.out_file
    print('input file is: {}'.format(in_file))
    print('output file is: {}'.format(out_file))

    engine_dict = {'baidu': read_baidu_config, 'yuan1.0': read_yuan1_0_config, 'zhiyuan': read_zhiyuan_config}
    ask_dict = {'baidu': baidu_ask, 'yuan1.0': yuan1_0_ask, 'zhiyuan': zhiyuan_ask}
    ans_dict = {'baidu': [], 'yuan1.0': [], 'zhiyuan': []}
    config_dict = {engine: engine_dict[engine]() for engine in engine_dict}
    for engine in config_dict:
        print('{} config is {}'.format(engine, config_dict[engine]))

    df = pd.read_csv(in_file, sep='\t')
    print(df.info())
    for q in tqdm(df['question_zh-cn']):
        for engine in engine_dict:
            try:
                print('question is: {},'.format(q), 'engine is: {}'.format(engine))
                config = config_dict[engine]
                ans = ask_dict[engine](q, *config)
                print('{} answer is: {}'.format(engine, ans))
            except Exception as e:
                print('Exception is {}, assign null value'.format(e))
                ans = ''
            finally:
                ans_dict[engine].append(ans)


    for engine in ans_dict:
        df[engine] = ans_dict[engine]
    df.to_csv(out_file, sep='\t', index=False)
    print('file saved to: {}'.format(out_file))


if __name__ == '__main__':
    main()
