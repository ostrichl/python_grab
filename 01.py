# -*- coding: utf-8 -*-

import urllib2 
import cookielib

url = "http://www.baidu.com"
#url = ''
print '01'

reponse1 = urllib2.urlopen(url)
print reponse1
#print reponse1.getcode()
#网页内容的长度
#print len(reponse1.read())


#print '02'
request1 = urllib2.Request(url)
print request1
#添加http的header
request1.add_header('User-Agent', 'Mozilla/5.0')
reponse2 = urllib2.urlopen(url)
#print reponse2.getcode()
#发送请求获取结果
#print len(reponse2.read())

#print '03'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
reponse3 = urllib2.urlopen(url)
#print cj
#print reponse3.read()