# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
import json
import logging


W_TOKEN = "chrisjiao"
AppID = "wx3caa80ff176f212e"
AppSecret = "e8281f1a5f854b560aed83e896c649a6"

wechat_instance = WechatBasic(
    token=W_TOKEN,
    appid=AppID,
    appsecret=AppSecret
)


@csrf_exempt
def index(request):
    if request.method == "GET":
        signature = request.GET.get("signature")
        timestamp = request.GET.get("timestamp")
        nonce = request.GET.get("nonce")

        if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest("Verify Faild")

        return HttpResponse(request.GET.get('echostr', ''), content_type="text/plain")
    logging.getLogger(__name__).info("POST")
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest("Invalid XML Data")

    message = wechat_instance.get_message()
    logging.getLogger(__name__).info(message)
    response = wechat_instance.response_text(
        content=(
            '感谢您的关注！\n回复【功能】两个字查看支持的功能，还可以回复任意内容开始聊天'
            ))
    if isinstance(message, TextMessage):
        # 当前会话内容
        content = message.content.strip()
        logging.getLogger(__name__).info(content)
        if content == '功能':
            reply_text = (
                '回复任意词语，查天气，陪聊天，讲故事，无所不能！\n'
                '还有更多功能正在开发中哦 ^_^\n'
            )
        elif content.endswith('天气'):
            city = content[:-2]
            weather_url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
            logging.getLogger(__name__).info(weather_url)
            response = requests.get(weather_url)
            data = json.loads(response.content)

            reply_text = (
                data['data']['forecast'][0]['high'] + '\n' +
                data['data']['forecast'][0]['high'] + '\n' +
                data['data']['forecast'][0]['type']
            )
        elif content == '讲故事':
            reply_text = (
                '儿子中考考试考差了，被老婆骂了一顿。\n''我去安慰儿子：“你要努力学习，以后一定要超越爸爸。”\n''儿子愣了一下，弱弱来了一句：“别的我不敢保证。但是，以后找个比你好的老婆还是很有把握的。”‍\n')
        else:
            reply_text = '啦啦啦啦啦啦啦'
        response = wechat_instance.response_text(content=reply_text)

    return HttpResponse(response, content_type="application/xml")

