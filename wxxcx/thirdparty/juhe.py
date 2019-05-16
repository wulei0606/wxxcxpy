import datetime
import json
import requests

# ----------------------------------
# 天气预报调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/73
# ----------------------------------
from utils import proxy


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


# ----------------------------------
# 股票数据调用示例代码 － 聚合数据
# 在线接口文档：https://www.juhe.cn/docs/api/id/21
# ----------------------------------

def stock(market, code):
    '''
    沪深股票
    :param market: 上交所 = sh, 深交所 = sz
    :param code: 股票编号
    :return:
    '''
    key = 'ad56142f0674fdd92addc7f6b27929de'
    api = 'http://web.juhe.cn:8080/finance/stock/hs'
    params = 'gid=%s&key=%s' % (market + code, key)
    url = api + '?' + params
    # print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    data = data.get('result')[0].get('data')
    response = {
        'name': data.get('name'),
        'now_price': data.get('nowPri'),
        'today_min': data.get('todayMin'),
        'today_max': data.get('todayMax'),
        'start_price': data.get('todayStartPri'),
        'date': data.get('date'),
        'time': data.get('time')
    }
    response['is_rising'] = data.get('nowPri') > data.get('todayStartPri')
    sub = abs(float(data.get('nowPri')) - float(data.get('todayStartPri')))  # 差值
    response['sub'] = float('%.3f' % sub)
    # print(response)
    return response


# ----------------------------------
# 星座运势调用示例代码 － 聚合数据
# 在线接口文档：https://www.juhe.cn/docs/api/id/58
# ----------------------------------

def constellation(cons_name):
    '''
    :param cons_name: 星座名字
    :return: json 今天运势
    '''
    key = '6fbdd81e8ee3682af60758fb14f3e5ce'
    api = 'http://web.juhe.cn:8080/constellation/getAll'
    types = ('today', 'tomorrow', 'week', 'month', 'year')
    params = 'consName=%s&type=%s&key=%s' % (cons_name, types[0], key)
    url = api + '?' + params
    # print(url)
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    return {
        'name': cons_name,
        'text': data['summary']
    }

# ----------------------------------
# 笑话大全调用示例代码 － 聚合数据
# 在线接口文档：https://www.juhe.cn/docs/api/id/58
# ----------------------------------
def joke():

    key = '3bbe01da9b3a5f398b3931876385ef75'
    url = 'http://v.juhe.cn/joke/content/text.php?key=%s&page=1&pagesize=20' % (key)
    # print(url)
    response = requests.get(url)
    data = json.loads(response.text)
    result = data['result']
    response_data = result['data']
    # print(response_data)
    return response_data

# if __name__ == '__main__':
#     joke()
    # data = stock('sz','000001')

