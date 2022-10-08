# ref: https://wenxin.baidu.com/moduleApi/ernie3
# -*- coding: utf-8 -*

import wenxin_api  # install via `pip install wenxin-api`
from wenxin_api.tasks.free_qa import FreeQA
import sys
import tomli


def baidu_ask(text, ak, sk):
    wenxin_api.ak = ak
    wenxin_api.sk = sk
    input_dict = {
        "text": "问题：{}\n回答：".format(text),
        "seq_len": 512,
        "topp": 0.5,
        "penalty_score": 1.2,
        "min_dec_len": 2,
        "min_dec_penalty_text": "。?：！",
        "is_unidirectional": 0,
        "task_prompt": "qa",
        "mask_type": "word"
    }
    rst = FreeQA.create(**input_dict)['result'].strip()
    return rst


def read_baidu_config():
    with open('../credentials/baidu.toml', mode='rb') as f:
        config = tomli.load(f)
    ak = config['api']['ak']
    sk = config['api']['sk']
    return ak, sk


def main():
    q = sys.argv[1] if len(sys.argv) > 1 else '做生意的基本原则是什么？'
    print('question is: {}'.format(q))
    ak, sk = read_baidu_config()
    res = baidu_ask(q, ak, sk)
    print(res)


if __name__ == '__main__':
    main()
