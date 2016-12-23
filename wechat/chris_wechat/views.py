# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.template import loader, Context
from xml.etree import ElementTree as ET
import time
import hashlib


class WeChat(View):
    # 这里我当时写成了防止跨站请求伪造，其实不是这样的，恰恰相反。因为django默认是开启了csrf防护中间件的
    # 所以这里使用@csrf_exempt是单独为这个函数去掉这个防护功能。
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(WeChat, self).dispatch(*args, **kwargs)

    def get(self, request):
        # 下面这四个参数是在接入时，微信的服务器发送过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        # 这个token是我们自己来定义的，并且这个要填写在开发文档中的Token的位置
        token = '这里的token需要自己设定，主要是和微信的服务器完成验证使用'

        # 把token，timestamp, nonce放在一个序列中，并且按字符排序
        hashlist = [token, timestamp, nonce]
        hashlist.sort()

        # 将上面的序列合成一个字符串
        hashstr = ''.join([s for s in hashlist])

        # 通过python标准库中的sha1加密算法，处理上面的字符串，形成新的字符串。
        hashstr = hashlib.sha1(hashstr).hexdigest()

        # 把我们生成的字符串和微信服务器发送过来的字符串比较，
        # 如果相同，就把服务器发过来的echostr字符串返回去
        if hashstr == signature:
            return HttpResponse(echostr)


















#
#
# from __future__ import unicode_literals
#
# import requests
# from django.http.response import HttpResponse, HttpResponseBadRequest
# from django.views.decorators.csrf import csrf_exempt
#
# from wechat_sdk import WechatBasic
# from wechat_sdk.exceptions import ParseError
# from wechat_sdk.messages import TextMessage
# import json
# from django.conf import settings
#
#
# wechat_instance = WechatBasic(
#     token=settings.WeChat_TOKEN,
#     appid=settings.AppID,
#     appsecret=settings.AppSecret
# )
#
#
# @csrf_exempt
# def index(request):
#     if request.method == "GET":
#         signature = request.GET.get("signature")
#         timestamp = request.GET.get("timestamp")
#         nonce = request.GET.get("nonce")
#
#         if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
#             return HttpResponseBadRequest("Verify Faild")
#
#         return HttpResponse(request.GET.get('echostr', ''), content_type="text/plain")
#
#     try:
#         wechat_instance.parse_data(data=request.body)
#     except ParseError:
#         return HttpResponseBadRequest("Invalid XML Data")
#
#     message = wechat_instance.get_message()
#
#     response = wechat_instance.response_text(
#         content=(
#             '感谢您的关注！\n回复【功能】两个字查看支持的功能，还可以回复任意内容开始聊天'
#             ))
#     if isinstance(message, TextMessage):
#         # 当前会话内容
#         content = message.content.strip()
#         print content
#         if content == '功能':
#             reply_text = (
#                 '回复任意词语，查天气，陪聊天，讲故事，无所不能！\n'
#                 '还有更多功能正在开发中哦 ^_^\n'
#             )
#         elif content.endswith('天气'):
#             city = content[:-2]
#             response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
#             data = json.loads(response.content)
#
#             reply_text = (
#                 data['data']['forecast'][0]['high'] + '\n' +
#                 data['data']['forecast'][0]['high'] + '\n' +
#                 data['data']['forecast'][0]['type']
#             )
#
#         response = wechat_instance.response_text(content=reply_text)
#
#     return HttpResponse(response, content_type="application/xml")
#
