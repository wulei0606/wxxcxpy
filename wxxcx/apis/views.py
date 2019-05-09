import json

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse,JsonResponse

from thirdparty import juhe

def helloworld(request):
    print('request method: ',request.method)
    print('request META: ',request.META)
    print('request cookies: ',request.COOKIES)
    print(request.GET)
    return HttpResponse('ok')


#天气接口
def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data = juhe.weather(city)
        return JsonResponse(data=data,status=200)
    elif request.method == 'POST':
        recived_body = request.body
        recived_body = json.loads(recived_body)
        cities = recived_body.get('cities')
        response_data = []
        for city in cities:
            result = juhe.weather(city)
            result['city'] = city
            response_data.append(result)
        return JsonResponse(data=response_data,safe=False,status=200)

    else:
        print('no supported method')