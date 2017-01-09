#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2017/1/9 14:18
"""
import logging
import requests
import json

logger = logging.getLogger("third")


def search_menu(key=u'红烧肉'):
    menu_url = "http://www.tngou.net/api/cook/name?name=%s" % key
    response = requests.get(menu_url)
    data = json.loads(response.content)

    try:
        menu_data = data.get("tngou")
        for row in menu_data:
            max_count = 0
            max_data = {}
            if row["count"] > max_count:
                max_count = row["count"]
                max_data = row

        name = max_data.get("name")
        description = max_data.get("description")
        food = max_data.get("food")
        img_url = "http://tnfs.tngou.net/image" + max_data.get("img")
        message = max_data.get("message")

        reply_text = message
    except Exception as e:
        logging.getLogger('third').exception(e)
        reply_text = '抱歉没有找到,赖我喽'
    return reply_text
