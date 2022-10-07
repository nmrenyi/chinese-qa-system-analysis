# api from https://open.wudaoai.com/trialcenter
from wudaoai.api_request import executeEngine, getToken # install with `pip install wudaoai`

'''
   获取接口鉴权token，请求参数 api_Key、 public_key 开放平台个人中心API Keys中获取。
   token有效期为8小时，建议放入缓存中不必每次请求获取，缓存失效时间设置小于8小时。
'''
# 接口API KEY
api_key = "your api key"
# 公钥
public_key = "your public key"
# 鉴权token
token = getToken(api_key, public_key)
# 能力类型
ability_type = "articleTitle"
# 引擎类型
engine_type = "title-creation"

data = {
    "prompt": "新闻 炸裂"  # 内容输入（必填）取值范围1～200
}
resp = executeEngine(ability_type, engine_type, token, data)

'''
    {
      "code": 200,  # 请求响应状态 200 为业务处理成功
      "msg": "成功",  # 错误信息
      "data": {
               "prompt": "新闻  炸裂",  # 用户输入项 
               "promptDesc": None, 
               "outputText": "!炸裂!炸裂!《炸裂》终于定档了,一起来看下吧...",  # 平台输出
               "inputTokenNum": 9,  # 输入词块数
               "outputTokenNum": 19, # 输出词块数
               "totalTokenNum": 28,  # 总词块数
               "taskOrderNo": "1000651508360039046451200", # 任务订单号
               "taskStatus":"SUCCESS"
               }, 
      "success": True
    }
'''
