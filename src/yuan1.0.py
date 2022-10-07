import requests
res = requests.get('http://221.194.179.88:11016/?question=中国第一位女皇帝是谁&usrname=hacker_anonymous&phone=17812007230')
print(res.text)
