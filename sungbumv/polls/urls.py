
# urlconf를 생성하기위한 파일

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]