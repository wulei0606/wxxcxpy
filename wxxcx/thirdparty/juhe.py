import datetime
import json
import requests

# ----------------------------------
# 天气预报调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/73
# ----------------------------------

def weather(cityname):

    key = 'cc9f4c500a45e2c41951267bf47fa3af'
    api = 'http://apis.juhe.cn/simpleWeather/query'

    params = 'city=%s&key=%s' % (cityname,key)
    url = api + '?' + params
    # print(url)

    response = requests.get(url=url)
    json_data = json.loads(response.text)
    # print(json_data)
    result = json_data['result']
    # print(result)
    sk = result['realtime']
    # print(sk)
    response = dict()
    response['city'] = cityname
    response['temperature'] = sk['temperature']
    response['info'] = sk['info']
    response['wid'] = sk['wid']
    response['humidity'] = sk['humidity']
    response['aqi'] = sk['aqi']
    response['direct'] = sk['direct']
    response['power'] = sk['power']
    response['nowtime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return response

# if __name__ == '__main__':
#     data = weather('广州')

