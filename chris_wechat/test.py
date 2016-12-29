#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2016/12/29 16:39
"""
import requests
import json


def reqq():
    constellation_en = 'leo'
    constellation_url = 'http://app.data.qq.com/?umod=astro&act=astro&jsonp=1&func=TodatTpl&t=4&a=%s' % constellation_en
    response = requests.get(constellation_url)
    print response
    data = json.loads(response.content.encode("utf-8").decode('unicode_escape')[9:][:-2])
    astro = data.get("astro")
    reply_text = ""
    for row in data.get("fortune"):
        _type = row.get("type")
        _content = row.get("content")
        reply_text += _type + ": " + _content + '\n'

    print reply_text
    print astro

if __name__ == "__main__":
    reqq()
