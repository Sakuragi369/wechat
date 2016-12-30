#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2016/12/30 17:49
"""
import requests
import json


def get_music(keyword):

    get_music_url = 'http://s.music.163.com/search/get/?type=1&s=%s&limit=1&offset=0' % keyword
    response = requests.get(get_music_url)
    data = json.loads(response.content).get('result').get('songs')[0]
    name = data.get("name")
    music_url = data.get("audio")
    id = data.get("id")

    return music_url, name, "", "", ""
