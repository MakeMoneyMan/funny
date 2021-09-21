import requests
from bs4 import BeautifulSoup
import json
import time

def order(cd1, cd2):
    url = "https://tytapp.quntitong.cn/sportinterNew/androidorder/saveOrder.do"
    data = '{"userID":"8a42f49278689f8f0178f8ff854a357a","cgId":"402881b441a660630141a712b12f0046","cgCode":"0020C061256","cgtype":"3","terminal":"10","openDate":"2021-09-24","ordertotal":"140","os":"wx","queryType":"android","lon":"113.3685116666855","lat":"23.130485599564228","subAdress":"","sportsNum":"5","citys":"440100","num' + cd1 + '":"1","num' + cd2 + '":"1","storeIds":"' + cd1 + '%2C'+ cd2 + '","quanid":""}'
    result = requests.post(url, data)
    print(result.text)

    # for item in jsonData:
    #     print(item.keys())
    #     print("--------------------------")


def check():
    url = "https://tytapp.quntitong.cn/sportinterNew/androidstadium/queryStoreByType.do"
    data = { "cgCode": "0020C061256", "sportCode": "003", "openDate": "2021-09-24", "booking": "Y", }

    result = requests.post(url, data)
    if(len(result.text) > 20):
        jsonData = json.loads(result.text)

        cd1 = ''
        cd2 = ''
        for item in jsonData:
            print(item['stadiumField']['fieldName'])
            if(item['stadiumField']['fieldName'] == '室外场地AA'):
                for storeItem in item['storeList']:
                    print(storeItem['startTime'])
                    if(storeItem['startTime'] == '10:00'):
                        cd1 = storeItem['resourceid']
                    if(storeItem['startTime'] == '11:00'):
                        cd2 = storeItem['resourceid']
                    if(len(cd1) > 10 and len(cd2) > 10):
                        print(item['stadiumField']['fieldName'])
                        order(cd1, cd2)
                        time.sleep(1)
                        order(cd1, cd2)
                        time.sleep(1)
                        order(cd1, cd2)
                        return
    else:
        check()
    #     print(result.text)
    #     order()
    # else:
    #     print("当前时间戳为:")
    #     print(time.time())
    #     time.sleep(1)
    #     check()


def main():
    timeHour = time.strftime("%H", time.localtime())
    if(timeHour == '13'):
        print(222)
        check()
        return True


while True:
    result = main()
    if result == True:
        break
    time.sleep(1)
    print(111)
# check()