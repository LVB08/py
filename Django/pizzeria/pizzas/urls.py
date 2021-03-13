"""定义pizzas的URL模式"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有披萨的种类
    url(r'^species/$', views.species, name='species'),

    # 显示特定披萨的配料
    url(r'^species/(?P<ine_id>\d+)/$', views.ine, name='ine'),
]