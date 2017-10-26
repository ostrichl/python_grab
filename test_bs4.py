# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import regex

#根据html网页字符串创建BeautifulSoup对象
html = """
<nav class="header-menu">
    <ul>
    
        <li><a href="/">主页</a></li>
    
        <li><a href="/tags/随笔/">随笔</a></li>
    
    </ul>
</nav>
<nav class="header-smart-menu">
    
        
        <a q-on="click: openSlider(e, 'innerArchive')" href="javascript:void(0)">所有文章</a>
        
    
        
        <a q-on="click: openSlider(e, 'friends')" href="javascript:void(0)">友链</a>
        
    
        
        <a q-on="click: openSlider(e, 'aboutme')" href="javascript:void(0)">关于我</a>
        
    
</nav>
<nav class="header-nav">
    <div class="social">
        
            <a class="github" target="_blank" href="#" title="github"><i class="icon-github"></i></a>
        
            <a class="weibo" target="_blank" href="#" title="weibo"><i class="icon-weibo"></i></a>
        
            <a class="rss" target="_blank" href="#" title="rss"><i class="icon-rss"></i></a>
        
            <a class="zhihu" target="_blank" href="#" title="zhihu"><i class="icon-zhihu"></i></a>
        
    </div>
</nav>

"""
#第二个参数为解析器 3指定编码
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

print 'allLink:'

links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

link_node = soup.find('a', href='/tags/随笔/')
print link_node.name, link_node['href'], link_node.get_text()

link_node1 = soup.find('a', href=regex.compile(r"tags"))
print link_node1.name, link_node1['href'], link_node1.get_text()

link_node2 = soup.find('a', class_='zhihu')
print link_node2.name, link_node2['href'], link_node2.get_text()