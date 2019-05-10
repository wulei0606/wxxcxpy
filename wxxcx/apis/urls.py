from django.urls import path


from apis.weather.menu import get_menu
from apis.weather.image import image

from apis.weather import views,menu,image

urlpatterns = [
    #天气信息
    path('weather',views.WeatherView.as_view(),name='weather'),
    #菜单
    path('menu',menu.get_menu,name='menu'),
    #图片
    # path('image', weather.image.image, name='image'),
    #
    path('imagetext',image.image_text,name='imagetext'),
    #类视图测试
    path('image',image.ImageView.as_view(),name='image')

]