#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2016/12/23 15:45
"""
from django.conf.urls import url
from chris_wechat import views

urlpatterns = [
    url(r'^$', views.index),
]
