# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 20:45
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_baseinfo.py

import requests

def http_request(method, url, param, header):
    if method.lower() == 'post':
        req = requests.post(url, json=param, headers=header)
    else:
        req = requests.get(url, json=param, headers=header)
    return req.json()

if __name__ == '__main__':


# 公用
    headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json;charset=UTF-8"}

    # # 注册
    # reg_url = "http://120.78.128.25:8766/futureloan/member/register"
    # reg_param = {"pwd": "12345678", "mobile_phone": "13517315121"}
    # result=http_request('post', reg_url, reg_param,headers)
    # print(result)

    # 登录
    login_url = "http://120.78.128.25:8766/futureloan/member/login"
    login_param = {"pwd": "12345678", "mobile_phone": "13517315121"}
    result = http_request('post', login_url, login_param, headers)
    print(result)

    # 获取token 和id
    token = result['data']['token_info']['token']
    member_id = result['data']['id']
    print("token值是：", token)
    print("member_id是：", member_id)

    # 充值
    login_header = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json;charset=UTF-8","Authorization":"Bearer "+token}
    recharge_url = "http://120.78.128.25:8766/futureloan/member/recharge"
    recharge_param = {"member_id": member_id, "amount": "1000"}
    result = http_request('post', recharge_url, recharge_param, login_header)
    print(result)
