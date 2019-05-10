#解析写好的yaml文件，根据文件给前端返回数据

import os
import yaml
from django.http import JsonResponse

from wxxcx import settings

from utils import appresponse

def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        return apps


def get_menu(request):
    global_app_data = init_app_data()
    publish_app_data = global_app_data.get('published')
    response = appresponse.wrap_json_response(data=publish_app_data,
                                              code=appresponse.ReturnCode.SUCCESS)

    return JsonResponse(data=response, safe=False)