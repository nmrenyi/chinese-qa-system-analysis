# ref: https://wenxin.baidu.com/moduleApi/ernie3
# -*- coding: utf-8 -*
import wenxin_api # 可以通过"pip install wenxin-api"命令安装
from wenxin_api.tasks.free_qa import FreeQA
wenxin_api.ak = "wmGvEfgS5DITADjfUqtt0Asoz6LmQzdc"
wenxin_api.sk = "7Oi0GigT0xYRLWZBrhAp4ZjKmgdq5Cs3"
input_dict = {
    "text": "问题：做生意的基本原则是什么？\n回答：",
    "seq_len": 512,
    "topp": 0.5,
    "penalty_score": 1.2,
    "min_dec_len": 2,
    "min_dec_penalty_text": "。?：！",
    "is_unidirectional": 0,
    "task_prompt": "qa",
    "mask_type": "word"
}
rst = FreeQA.create(**input_dict)
print(rst)
