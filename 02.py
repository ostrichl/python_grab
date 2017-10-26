# -*- coding: utf-8 -*-
import urllib2

#创建request对象
request = urllib2.Request('https://www.zhihu.com/')

#添加数据
request.add_data('a', '2')
#添加http的header
request.add_header('User-Agent', 'Mozilla/5.0')
#发送请求获取结果
response = urllib2.urlopen(request)