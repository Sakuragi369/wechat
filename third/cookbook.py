#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2017/1/9 14:18
"""
import logging
import requests
import json

logger = logging.getLogger(__name__)


def search_menu(key=u'西红柿炒鸡蛋'):
    menu_url = "http://www.tngou.net/api/cook/name?name=%s" % key
    response = requests.get(menu_url)
    data = json.loads(response.content)

    try:
        menu_data = data.get("tngou")
        for row in menu_data:
            max_count = 0
            max_data = {}
            if row["count"] > max_count:
                max_data = row

        name = max_data.name
        description = max_data.description
        food = max_data.food
        img_url = "http://tnfs.tngou.net/image" + max_data.img
        message = max_data.message

        reply_text = message
    except Exception as e:
        logger.exception(e)
        reply_text = '抱歉没有找到,赖我喽'
    return reply_text

