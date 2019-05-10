import hashlib
import  os
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from django.views import View

from utils.appresponse import ReturnCode
from wxxcx import settings
from utils import appresponse

def image(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return Http404()
        else:
            data = open(imgfile, 'rb').read()
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')
            # return HttpResponse(content=data, content_type='image/jpg')


class ImageView(View,appresponse.CommonResponseMixin):
    def get(self,request):
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return Http404()
        else:
            data = open(imgfile, 'rb').read()
            return FileResponse(open(imgfile, 'rb'), content_type='image/jpg')

    def post(self,request):
        files = request.FILES
        response=[]
        for key,value in files.items():
            content = value.read()
            md5 = hashlib.md5(content).hexdigest()
            path = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
            with open(path, 'wb') as f:
                f.write(content)
            response.append({
                'name': key,
                'md5' : md5
            })

        message = 'post message'
        response = self.wrap_json_response(data=response,code=ReturnCode.SUCCESS,message=message)
        # print(response)
        return JsonResponse(data=response, safe=False)

    def delete(self,request):
        md5 = request.GET.get('md5')
        img_name = md5 + '.jpg'
        path = os.path.join(settings.IMAGES_DIR,img_name)
        if os.path.exists(path):
            os.remove(path)
            message = 'remove success'
        else:
            message = 'file (%s) not found .' % img_name
            response= self.wrap_json_response(code=ReturnCode.SUCCESS, message=message)
            return JsonResponse(data=response, safe=False)






def image_text(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.IMAGES_DIR, md5 + '.jpg')
        if not os.path.exists(imgfile):
            return appresponse.wrap_json_response(
                code=appresponse.ReturnCode.RESOURCES_NOT_EXISTS
            )
        else:
            response_data = {}
            response_data['name'] = md5 + '.jpg'
            response_data['url'] = '/services/image?md5=%s' % (md5)
            response = appresponse.wrap_json_response(data=response_data)
            return JsonResponse(data=response, safe=False)
