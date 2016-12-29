#!/usr/bin/env python
# coding: utf-8

"""
@author: jian.jiao

@time: 2016/12/29 16:18
"""
constellation_dict = {
    "狮子座": "Leo",
    "双子座": "Gemini",
    "金牛座": "Taurus",
    "白羊座": "Aries",
    "巨蟹座": "Cancer",
    "处女座": "Virgo",
    "天秤座": "Libra",
    "天蝎座": "Scorpio",
    "射手座": "Sagittarius",
    "摩羯座": "Capricorn",
    "水瓶座": "Aquarius",
    "双鱼座": "Pisces",
}

# 故事集合
STORY = {
    1: '儿子中考考试考差了，被老婆骂了一顿。' + '\n' +
       '我去安慰儿子：“你要努力学习，以后一定要超越爸爸。” ' + '\n' +
       '儿子愣了一下，弱弱来了一句：“别的我不敢保证。但是，以后找个比你好的老婆还是很有把握的。”‍' + '\n',
    2: "今天中午弟弟突然找我要钱，我问他要钱干啥？" + "\n" +
       "弟弟有些扭捏的回道:“这不‘六一’快要到了吗，我想给我喜欢的一女同学买件礼物。”" + "\n" +
       "我心想:“你哥我到现在还单着呢，你这么小就要搞对象，太不像话了。”于是义正言辞的拒绝道:“不行，你要以学习为重。”" + "\n" +
       "正当弟弟有些很失落，老妈不知道从哪跑了过来，怒声道:“别搭理你哥，这钱妈给！”",
    3: "宝宝在喝水，摔了一下，不小心把水撒在地板上了，哭的好伤心，我没理她，也没管她……" + "\n" +
       "其实我觉得自己摔倒应该自己爬起来，毕竟我不可能时时刻刻守护着她，所以我没理她……" + "\n" +
       "可是她看到我没理她过后，自己爬起来，就去找了条毛巾，一边哭一边擦地板……",
    4: "刚刚在筛简历的时候,看到某毕业生简历--获奖经历：在校期间多次获得康师傅“再来一瓶”奖励。",
    5: "听来的，某人去东北出差，在饭馆要啤酒，服务员问，您要常温的还是冷藏的？ 某人怒道，这大冷天的你还让我喝冷藏的？！ 服务员淡定的说，常温的零下15°，冷藏的零下1°",
    6: "大学时，一次老师让填一份很重要的表格，而且声明每人一张，没有富余的，不能涂改。一哥们上来就填，结果发现把民族“汉”填到了性别栏内，因为说了不让涂改，想了想，很NB地在“汉”后面加了个“子”字。",
    7: "有个兄弟追女朋友，每天早上一包心形饼干和一瓶牛奶。坚持不懈，终于到手。一天早上他又带着心形饼干去看女朋友，女友就问：“你这饼干哪买的？我去了好多超市，就是买不到这种形状的。”他自豪道：“那当然找不到啦，这是我啃出来的……”",
    8: "坐地铁，一小女孩在我的背后拿根魔杖玩，她拿着魔杖指着我的后背：我要把你变丑！我听完，笑了，转身过去就听到一声惊叫：妈妈！妈妈！我会魔法了！"
}
