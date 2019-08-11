import json
from .token import *


class Menu(object):
    def __init__(self):
        self.menue = {
            "button": [
                {
                    "type": "click",
                    "name": "公司相关",
                    "key": "COMPANY_INFO",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "公司官网",
                            "url": "http://www.soso.com/"
                        },
                        {
                            "type": "view",
                            "name": "产品介绍",
                            "url": "http://www.soso.com/"
                        }
                    ]
                },
                {
                    "type": "click",
                    "name": "设备管理",
                    "key": "DEVICE_MANAGER",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "所有设备",
                            "url": "http://www.soso.com/"
                        },
                        {
                            "type": "scancode_push",
                            "name": "添加设备",
                            "key": "ADD_DEVICE"
                        }
                    ]
                },
                {
                    "type": "click",
                    "name": "个人中心",
                    "key": "PERSONAL_INFO",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "个人主页",
                            "url": "http://103.219.38.145/user/"
                        },
                        {
                            "type": "view",
                            "name": "测试",
                            "url": "http://103.219.38.145/user/test/"
                        }
                    ]
                }
            ]
        }

    def create(self):
        data = json.dumps(self.menue, ensure_ascii=False)
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % get_token()
        req = requests.post(url, data.encode('utf-8'))
        print(req.text)
