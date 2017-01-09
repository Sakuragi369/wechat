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
from .backend import constellation_dict
from story.views import get_story
from third.weather import get_current_weather
from third.music import get_music
from third.cookbook import search_menu

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
            logging.getLogger(__name__).info("###" + city)
            reply_text = get_current_weather(city)

        elif content == '讲故事':
            story = get_story()
            reply_text = story

        elif content in constellation_dict.keys():
            constellation_en = constellation_dict.get(content, None).lower()
            constellation_url = 'http://app.data.qq.com/?umod=astro&act=astro&jsonp=1&func=TodatTpl&t=4&a=%s' % constellation_en
            response = requests.get(constellation_url)
            data = json.loads(response.content.encode("utf-8").decode('unicode_escape')[9:][:-2])
            reply_text = ""
            for row in data.get("fortune"):
                _type = row.get("type")
                _content = row.get("content")
                reply_text += _type + ": " + _content + '\n'

        elif content.startswith('音乐'):
            message = content[2:]
            music_url, title, description, _, _ = get_music(message)
            response = wechat_instance.response_music(music_url, title, description)
            return HttpResponse(response, content_type="application/xml")

        elif content.endswith("菜谱"):
            message = content[:2]
            reply_text = search_menu(message)
        else:
            reply_text = '啦啦啦啦啦啦啦'
        response = wechat_instance.response_text(content=reply_text)

    return HttpResponse(response, content_type="application/xml")
