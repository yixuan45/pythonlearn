# -*- coding: utf-8 -*-
import requests

# 会话
session = requests.session()
data = {
    "loginName": "17729686779",
    "password": "q6035945"
}
# 1.登录
url = "https://passport.17k.com/ck/user/login"
response = session.post(url, data=data)
print(response.text)
print(response.cookies)  # session相当于一个会话，有上下文的作用，这里模拟登陆过后，会有登录记录，会携带着cookies
# 2.拿书架上的数据
url = "https://www.17k.com/"
response = session.get(url)
print(response)
