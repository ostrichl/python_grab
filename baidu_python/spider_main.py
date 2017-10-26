#encoding:utf-8

import urllib2
import download_manage
import output_manage
import url_manage
import parse_manage


class SpiderMain(object):
    # 初始化四个解析器
    def __init__(self):
        self.url_manage = url_manage.UrlManger()
        self.download_manage = download_manage.DownLoadManager()
        self.parse_manage = parse_manage.ParseManager()
        self.output_manage = output_manage.OutPutManager()

    # 调度程序
    def craw(self, root_url):
        self.url_manage.add_new_url(root_url)
        count = 1;
        # 有待爬取的url
        while self.url_manage.has_new_url():
           try:
               new_url = self.url_manage.get_new_url()
               html_con = self.download_manage.download_html(new_url)
               # 解析出url和数据
               new_urls, data_dict = self.parse_manage.parse_html(new_url, html_con)
               self.url_manage.add_new_urls(new_urls)
               self.output_manage.collect_data(data_dict)
               print  "%d   %s" % (count, new_url)
               if count > 20:
                   break
               count = count + 1
           except:
               print "craw fail"


        self.output_manage.output_html()
        # self.output_manage.output_mysql()
# main函数
if __name__ == "__main__":
    # 入口url
    root_url = 'http://baike.baidu.com/item/Python'
    spider_main = SpiderMain()
    spider_main.craw(root_url)