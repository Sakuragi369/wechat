#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: jian.jiao

@time: 2016/12/30 16:22
"""
import logging
import requests
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger(__name__)


def get_current_weather(city=u'北京'):
    """获取当前天气情况"""
    weather_url = 'https://api.thinkpage.cn/v3/weather/now.json?key=qtvi7xhcjyjgtyte&location=%s&language=zh-Hans&unit=c' % city
    logger.info("########")
    logger.info(weather_url)
    logger.info("########")
    response = requests.get(weather_url)
    data = json.loads(response.content)
    try:
        location = data.get('results')[0].get('location').get("path")[:-3]
        temperature = data.get('results')[0].get('now').get("temperature")
        text = data.get('results')[0].get('now').get("text")

        reply_text = "城市:" + city + '\n' + "地理位置: " + location + "\n" + "天气: " + text + '\n' + "温度: " + temperature + "℃"

    except Exception as e:
        logger.exception(e)
        reply_text = '抱歉没有找到该城市'

    return reply_text


if __name__ == "__main__":
    get_current_weather()
