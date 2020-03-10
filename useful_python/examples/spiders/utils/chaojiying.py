#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5

class ChaojiyingClient(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)

        return r.json()



chaojiying = ChaojiyingClient('xiawuwudiande', '.D6GxxH8EYCeNUz',
                                  '2e8dab96655db7fa4ef01841c323907c')
def post_pic(im):


    # im = open('b.png', 'rb').read()
    ret = chaojiying.PostPic(im, 6001)
    print(ret)

    return ret

def error(im_id):
    ret = chaojiying.ReportError(im_id)

    print(ret)

    return ret



if __name__ == '__main__':
    chaojiying = ChaojiyingClient('xiawuwudiande', '.D6GxxH8EYCeNUz', '2e8dab96655db7fa4ef01841c323907c')	#用户中心>>软件ID 生成一个替换 96001
    # im = open('a.jpg', 'rb').read()
    # print(chaojiying.PostPic(im, 1902))


    im = open('b.png', 'rb').read()
    print(chaojiying.PostPic(im, 6001))

