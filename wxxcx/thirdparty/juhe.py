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
    result = json_data.get('result')
    # print(result)
    sk = result.get('realtime')
    response = dict()
    response['temperature'] = sk.get('temperature')
    response['info'] = sk.get('info')
    response['wid'] = sk.get('wid')
    response['humidity'] = sk.get('humidity')
    response['aqi'] = sk.get('aqi')
    return response

# if __name__ == '__main__':
#     data = weather('广州')

