import requests

url = 'https://www.quntitong.cn/sportinterNew/androidstadium/queryStoreByType.do'
data = {
    'cgCode': '0020C061256',
    'sportCode': '003',
    'openDate': '2023-04-27',
    'booking': 'Y',
    'sign': '98E0160753A22F8916F9A81BE5C70782'
}
headers = {
    'referer': 'https://servicewechat.com/wxe350a6af6d22b9e8/111/page-frame.html',
    'xweb_xhr': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6763',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh'
}

response = requests.post(url, data=data, headers=headers)

print(response.text)
