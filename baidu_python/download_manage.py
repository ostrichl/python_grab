#encoding:utf-8
import urllib2

class DownLoadManager(object):
    def download_html(self, new_url):
        if new_url is None:
            return None
        resp = urllib2.urlopen(new_url)
        # 请求失败
        if resp.getcode() != 200:
            return  None
        # 返回下载好的内容
        return resp.read()