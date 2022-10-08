import argparse
import sys

import pandas as pd
from baidu import read_baidu_config, baidu_ask
from zhiyuan import read_zhiyuan_config, zhiyuan_ask
from yuan1_0 import read_yuan1_0_config, yuan1_0_ask


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--engine', type=str, default='baidu', help='baidu, yuan1.0, zhiyuan')
    parser.add_argument('--question', type=str, default='中国的第一位女皇帝是谁', help='question')
    return parser.parse_args()


def main():
    args = parse_args()
    q = args.question
    engine = args.engine
    print('engine is: {}'.format(engine))
    print('question is: {}'.format(q))

    engine_dict = {'baidu': read_baidu_config, 'yuan1.0': read_yuan1_0_config, 'zhiyuan': read_zhiyuan_config}
    ask_dict = {'baidu': baidu_ask, 'yuan1.0': yuan1_0_ask, 'zhiyuan': zhiyuan_ask}

    config = engine_dict[engine]()
    print('config is: {}'.format(config))

    res = ask_dict[engine](q, *config)
    print(res)


if __name__ == '__main__':
    main()
