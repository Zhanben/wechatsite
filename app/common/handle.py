#! /usr/bin python
# coding: utf8
import time
import xml.etree.ElementTree as etree


class Msg(object):
    def __init__(self, et):
        self.From = et.find("FromUserName").text
        self.To = et.find("ToUserName").text
        self.MsgType = et.find("MsgType").text
        # 纯文字信息字段
        self.Content = et.find("Content").text if et.find("Content") is not None else ""
        # 语音信息字段
        self.Recognition = et.find("Recognition").text if et.find("Recognition") is not None else ""
        self.Format = et.find("Format").text if et.find("Format") is not None else ""
        self.MsgId = et.find("MsgId").text if et.find("MsgId") is not None else ""
        # 图片
        self.PicUr = et.find("PicUrl").text if et.find("PicUrl") is not None else ""
        self.MediaI = et.find("MediaId").text if et.find("MediaId") is not None else ""
        # 事件
        self.Event = et.find("Event").text if et.find("Event") is not None else ""


class MsgParser(object):
    """
    用于解析从微信公众平台传递过来的参数，并进行解析,返回一个消息类
    """

    def __init__(self, data):
        self.et = etree.fromstring(data)

    def parse(self):
        return Msg(self.et)


class MsgDispatcher(object):
    """
    根据消息的类型，获取不同的处理返回值
    """

    def __init__(self, data):
        self.msg = MsgParser(data).parse()
        self.handler = MsgHandler()

    def dispatch(self):
        handle_map = {
            "text": self.handler.text_handle,
            "voice": self.handler.voice_handle,
            "image": self.handler.image_handle,
            "video": self.handler.video_handle,
            "shortvideo": self.handler.shortVideo_handle,
            "location": self.handler.location_handle,
            "link": self.handler.link_handle,
            "event": self.handler.event_handle,
        }
        handler = handle_map.get(self.msg.MsgType)
        if handler is not None:
            result = handler(self.msg)
            return result
        else:
            return ""


class MsgHandler(object):
    """
    针对type不同，转交给不同的处理函数。直接处理即可
    """

    def __init__(self):
        self.time = int(time.time())

    def text_handle(self, msg, user='', master='', time='', content=''):
        template = """
         <xml>
          <ToUserName><![CDATA[{}]]></ToUserName>
          <FromUserName><![CDATA[{}]]></FromUserName>
          <CreateTime>{}</CreateTime>
          <MsgType><![CDATA[text]]></MsgType>
          <Content><![CDATA[{}]]></Content>
          </xml>
         """
        # 对用户发过来的数据进行解析，并执行不同的路径
        try:
            response = get_response_by_keyword(msg.content)
            print("%s", response)
            if response['type'] == "image":
                result = self.image_handle(msg, msg.user, msg.master, self.time, response['content'])
            elif response['type'] == "music":
                data = response['content']
                result = self.music_handle(data['title'], data['description'], data['url'], data['hqurl'])
            elif response['type'] == "news":
                items = response['content']
                result = self.news_handle(items)
                # 这里还可以添加更多的拓展内容
            else:
                response = "no support"
                result = template.format(msg.user, msg.master, self.time, response)
        except Exception as e:
            with open("./debug.log", 'a') as f:
                f.write("text _handler:" + str(e.message))
                f.close()
        return result

    def music_handle(self, msg, title='', description='', url='', hqurl=''):

        template = """
         <xml>
          <ToUserName><![CDATA[{}]]></ToUserName>
          <FromUserName><![CDATA[{}]]></FromUserName>
          <CreateTime>{}</CreateTime>
          <MsgType><![CDATA[music]]></MsgType>
          <Music>
          <Title><![CDATA[{}]]></Title>
          <Description><![CDATA[{}]]></Description>
          <MusicUrl><![CDATA[{}]]></MusicUrl>
          <HQMusicUrl><![CDATA[{}]]></HQMusicUrl>
          </Music>
          <FuncFlag>0</FuncFlag>
         </xml>
         """
        response = template.format(msg.user, msg.master, self.time, title, description, url, hqurl)
        return response

    def voice_handle(self, msg):
        response = get_turing_response(msg[""])
        result = self.text_handle(msg.user, msg.master, self.time, response)
        return result

    def image_handle(self, msg, user='', master='', time='', mediaid=''):
        template = """
         <xml>
          <ToUserName><![CDATA[{}]]></ToUserName>
          <FromUserName><![CDATA[{}]]></FromUserName>
          <CreateTime>{}</CreateTime>
          <MsgType><![CDATA[image]]></MsgType>
          <Image>
          <MediaId><![CDATA[{}]]></MediaId>
          </Image>
          </xml>
         """
        if mediaid == '':
            response = msg.mediaid
        else:
            response = mediaid
        result = template.format(msg.user, msg.master, self.time, response)
        return result

    def video_handle(self):
        return 'video'

    def shortVideo_handle(self):
        return 'shortvideo'

    def location_handle(self):
        return 'location'

    def link_handle(self):
        return 'link'

    def event_handle(self):
        return 'event'

    def news_handle(self, msg, items):
        # 图文消息这块真的好多坑，尤其是<![CDATA[]]>中间不可以有空格，可怕极了
        articlestr = """
         <item>
          <Title><![CDATA[{}]]></Title>
          <Description><![CDATA[{}]]></Description>
          <PicUrl><![CDATA[{}]]></PicUrl>
          <Url><![CDATA[{}]]></Url>
         </item>
         """
        itemstr = ""
        for item in items:
            itemstr += str(articlestr.format(item['title'], item['description'], item['picurl'], item['url']))
        template = """
         <xml>
          <ToUserName><![CDATA[{}]]></ToUserName>
          <FromUserName><![CDATA[{}]]></FromUserName>
          <CreateTime>{}</CreateTime>
          <MsgType><![CDATA[news]]></MsgType>
          <ArticleCount>{}</ArticleCount>
          <Articles>{}</Articles>
         </xml>
         """
        result = template.format(msg.user, msg.master, self.time, len(items), itemstr)
        return result


def get_turing_response(req=""):
    return ""


def get_qingyunke_response(req=""):
    return ""


# 简单做下。后面慢慢来
def get_response_by_keyword(keyword):
    if '团建' in keyword:
        result = {"type": "image", "content": "3s9Dh5rYdP9QruoJ_M6tIYDnxLLdsQNCMxkY0L2FMi6HhMlNPlkA1-50xaE_imL7"}
    elif 'music' in keyword or '音乐' in keyword:
        musicurl = 'http://204.11.1.34:9999/dl.stream.qqmusic.qq.com/C400001oO7TM2DE1OE.m4a?vkey=3DFC73D67AF14C36FD1128A7ABB7247D421A482EBEDA17DE43FF0F68420032B5A2D6818E364CB0BD4EAAD44E3E6DA00F5632859BEB687344&guid=5024663952&uin=1064319632&fromtag=66'
        result = {"type": "music",
                  "content": {"title": "80000", "description": "有个男歌手姓巴，他的女朋友姓万，于是这首歌叫80000", "url": musicurl,
                              "hqurl": musicurl}}
    elif '关于' in keyword:
        items = [{"title": "关于我", "description": "喜欢瞎搞一些脚本",
                  "picurl": "https://avatars1.githubusercontent.com/u/12973402?s=460&v=4",
                  "url": "https://github.com/guoruibiao"},
                 {"title": "我的博客", "description": "收集到的，瞎写的一些博客",
                  "picurl": "http://avatar.csdn.net/0/8/F/1_marksinoberg.jpg",
                  "url": "http://blog.csdn.net/marksinoberg"},
                 {"title": "薛定谔的:dog:", "description": "副标题有点奇怪，不知道要怎么设置比较好",
                  "picurl": "https://www.baidu.com/img/bd_logo1.png", "url": "http://www.baidu.com"}
                 ]
        result = {"type": "news", "content": items}
    else:
        result = {"type": "no support", "content": "items"}
    return result
