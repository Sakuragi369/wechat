#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2016/12/30 10:46
"""
from django.contrib import admin
from story import models
admin.site.register(models.Story)
