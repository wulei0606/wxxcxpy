import json

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse,JsonResponse
from django.views import View
from utils.appresponse import CommonResponseMixin
from thirdparty import juhe

#天气接口实现
class WeatherView(View,CommonResponseMixin):
    def get(self,request):
        pass
    def post(self,request):

        recived_body = request.body
        recived_body = json.loads(recived_body)
        cities = recived_body.get('cities')
        data = []
        # print(cities)
        for city in cities:
            # print(city)
            # print(city['city'])
            result = juhe.weather(city['city'])
            # print(result)
            result['city_info'] = city
            data.append(result)

        response_data = self.wrap_json_response(data=data)
        return JsonResponse(data=response_data, safe=False)


