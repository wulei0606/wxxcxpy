import json

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views import View
from utils.appresponse import CommonResponseMixin,ReturnCode
from utils.auth import c2s


from .models import User

def test_session(request):
    request.session['message'] = 'test django sessoin ok'
    response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)

class UserView(View,CommonResponseMixin):
    def get(self,request):
        pass

    def post(self,request):
        pass



def __authorize_by_code(request):
    '''
    使用wx.login得到临时code到微信提供的code2session接口授权
    post_data = {
        'encryptedData': 'xxxx',
        'appId': 'xxx',
        'sessionKey':'xxx',
        'iv' : 'xxx'
    }
    :param request:
    :return:
    '''
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    code = post_data.get('code').strip()
    app_id = post_data.get('appId').strip()
    nickname = post_data.get('nickname').strip()

    response = {}
    if not code or not app_id:
        response['message'] = 'authorize failed, need entire authoriation data'
        response['code'] = ReturnCode.BROKEN_AUTHORIZED_DATA
        return JsonResponse(data=response, safe=False)

    data = c2s(app_id, code)
    openid = data.get('openid')
    print(openid)
    if not openid:
        response = CommonResponseMixin.wrap_json_response(code=ReturnCode.FAILED, message='auth failes')
        return JsonResponse(data=response, safe=False)

    request.session['open_id'] = openid
    request.session['is_authorized'] = True

    if not User.objects.filter(open_id=openid):
        new_user  = User(open_id=openid, nickname=nickname)
        new_user.save()

    response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS, message='auth success')
    return JsonResponse(data=response, safe=False)



def authorize(request):
    return __authorize_by_code(request)

def test_session2(request):
    print(request.session.items())
    response = CommonResponseMixin.wrap_json_response(code=ReturnCode.SUCCESS)
    return JsonResponse(data=response, safe=False)