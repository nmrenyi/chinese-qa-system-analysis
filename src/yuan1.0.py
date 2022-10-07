import requests
import sys
import tomli


def main():
    q = sys.argv[1] if len(sys.argv) > 1 else '中国第一位女皇帝是谁？'
    print('question is: {}'.format(q))
    with open('../credentials/yuan1.0.toml', mode='rb') as f:
        config = tomli.load(f)
    username = config['api']['username']
    telephone = config['api']['telephone']
    print(yuan1_0_ask(q, username, telephone))


def yuan1_0_ask(q: str, username, telephone):
    res = requests.get('http://221.194.179.88:11016/', params={'question': q, 'usrname': username, 'phone': telephone})
    return res.text


if __name__ == '__main__':
    main()
