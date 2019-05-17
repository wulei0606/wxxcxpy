from django.urls import path

from .views import test_session,test_session2,UserView,authorize

urlpatterns = [
    path('test', test_session),
    path('test2', test_session2),
    path('user', UserView.as_view()),
    path('authorize',authorize),
]