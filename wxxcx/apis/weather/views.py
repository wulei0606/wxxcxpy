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
        for city in cities:
            result = juhe.weather(city)
            data.append(result)

        data = self.wrap_json_response(data=data)
        return JsonResponse(data=data, safe=False)


