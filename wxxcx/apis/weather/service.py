from thirdparty import juhe

from utils.appresponse import CommonResponseMixin,ReturnCode
from django.http import JsonResponse

popular_stocks = [
    {
        'code':'000001',
        'name':'平安银行',
        'market':'sz'
    },
    {
        'code': '000002',
        'name': '万科A',
        'market': 'sz'
    },
    {
        'code': '600036',
        'name': '招商银行',
        'market': 'sh'
    },
    {
        'code': '601398',
        'name': '工商银行',
        'market': 'sh'
    },
]

#股票数据接口
def stock(request):
    data = []
    for stock in popular_stocks:
        result = juhe.stock(market=stock['market'],code=stock['code'])
        data.append(result)
    response = CommonResponseMixin.wrap_json_response(data=data,code=ReturnCode.SUCCESS)
    return JsonResponse(data= response, safe= False)



constellations = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']

#星座运势接口
def constellation(request):
    data = []
    for c in constellations:
        result = juhe.constellation(c)
        data.append(result)
    response = CommonResponseMixin.wrap_json_response(data=data,code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)

#笑话接口
def joke(request):
    data = juhe.joke()
    # print(data)
    response = CommonResponseMixin.wrap_json_response(data=data,code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)