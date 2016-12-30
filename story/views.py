# -*- coding: utf-8 -*-
"""用户输入讲故事，随机返回一个数据库中的故事."""
from story.models import Story
import random


def get_story():
    max_story = len(Story.objects.all())
    _id = random.randint(1, max_story)
    story = Story.objects.filter(id=_id).first()

    return story.content
