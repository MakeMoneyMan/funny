import requests

# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://servicewechat.com/wxe350a6af6d22b9e8/47/page-frame.html',
}

# 请求正文中的参数
data = {
    'userID': '8a42f49278689f8f0178f8ff854a357a',
    'cgId': '402881b441a660630141a712b12f0046',
    'cgCode': '0020C061256',
    'cgtype': '3',
    'openDate': '2021-09-22',
    'ordertotal': '120',
    'queryType': 'android',
    'storeIds': '8a42f4877bf3f4c5017bfec9a42b1064,8a42f4877bf3f4c5017bfec9a42b1065',
    'citys': '440100',
}

# 发送POST请求
response = requests.post('https://tytapp.quntitong.cn/sportinterNew/androidorder/checkOrder.do', headers=headers, data=data)

# 输出响应内容
print(response.text)






