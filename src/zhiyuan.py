# api from https://open.wudaoai.com/trialcenter
from wudaoai.api_request import executeEngine, getToken  # install with `pip install wudaoai`
import sys
import tomli

'''
   获取接口鉴权token，请求参数 api_Key、 public_key 开放平台个人中心API Keys中获取。
   token有效期为8小时，建议放入缓存中不必每次请求获取，缓存失效时间设置小于8小时。
'''


def main():
    q = sys.argv[1] if len(sys.argv) > 1 else '世界的终极意义是什么？'
    print('question is: {}'.format(q))
    with open('../credentials/zhiyuan.toml', mode='rb') as f:
        config = tomli.load(f)
    api_key = config['api']['api_key']
    public_key = config['api']['public_key']
    token = getToken(api_key, public_key)
    res = zhiyuan_ask(q, token)
    print(res)


def zhiyuan_ask(q: str, token):
    # 能力类型
    ability_type = "question_answer"
    # 引擎类型
    engine_type = "txl-general-engine-v1"

    data = {
        "topP": 1,  # 核采样（必填）取值范围0～1
        "topK": 3,  # 采样（必填）取值范围0～10
        "temperature": 1,  # 概率分布调节（必填)取值范围0.5～1
        "presencePenalty": 1,  # 重复词去除（必填)取值范围0～20
        "frequencyPenalty": 1,  # 重复惩罚参数（必填)取值范围0～3
        "generatedLength": 128,  # 文本生成最大长度（必填)取值范围1～512
        "prompt": q,  # 标题关键词（必填）取值范围1～200
    }
    resp = executeEngine(ability_type, engine_type, token, data)
    res = resp['data']['outputText'].strip()
    return res


if __name__ == '__main__':
    main()
