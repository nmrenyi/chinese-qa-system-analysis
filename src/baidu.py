# ref: https://wenxin.baidu.com/moduleApi/ernie3
# -*- coding: utf-8 -*

import wenxin_api # install via `pip install wenxin-api`
from wenxin_api.tasks.free_qa import FreeQA
import sys

def baidu_ask(text):
    wenxin_api.ak = "wmGvEfgS5DITADjfUqtt0Asoz6LmQzdc"
    wenxin_api.sk = "7Oi0GigT0xYRLWZBrhAp4ZjKmgdq5Cs3"
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
    rst = FreeQA.create(**input_dict)['result']
    return rst

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else '做生意的基本原则是什么？'
    baidu_ask(q)
