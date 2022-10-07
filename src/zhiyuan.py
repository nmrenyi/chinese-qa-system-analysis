# api from https://open.wudaoai.com/trialcenter
from wudaoai.api_request import executeEngine, getToken  # install with `pip install wudaoai`

'''
   获取接口鉴权token，请求参数 api_Key、 public_key 开放平台个人中心API Keys中获取。
   token有效期为8小时，建议放入缓存中不必每次请求获取，缓存失效时间设置小于8小时。
'''
# 接口API KEY
api_key = "626ca361df7e4a4b9fc92ded56a67d93"
# 公钥
public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAOoF6XHqAlnKvMi4UiCPolnaG8okQ3l0o34gWmbIl1ABdEpUX3sDpwXO6e4SAejZEE48WTLXmhWkfRAgr2gm1h8CAwEAAQ=="
# 鉴权token
token = getToken(api_key, public_key)
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
    "prompt": "世界的终极意义是什么？",  # 标题关键词（必填）取值范围1～200
}
resp = executeEngine(ability_type, engine_type, token, data)

