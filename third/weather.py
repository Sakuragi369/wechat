#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2016/12/30 16:22
"""
import logging
import requests
import json


logger = logging.getLogger(__name__)


def get_current_weather(city=u'北京'):
    """获取当前天气情况"""
    weather_url = 'https://api.thinkpage.cn/v3/weather/now.json?key=qtvi7xhcjyjgtyte&location=%s&language=zh-Hans&unit=c' % city
    logger.info("########")
    logger.info(weather_url)
    logger.info("########")
    response = requests.get(weather_url)
    data = json.loads(response.content)

    temperature = data.get('results')[0].get('now').get("temperature")
    text = data.get('results')[0].get('now').get("text")

    reply_text = city + '\n' + u"天气: " + text + '\n' + u"温度: " + temperature + "℃"

    return reply_text
