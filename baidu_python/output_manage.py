#encoding:utf-8

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class OutPutManager(object):
    def __init__(self):
        self.html_datas = []

    def output_html(self):
        f = open("summary.html","w")
        #ascii
        f.write("<html>")
        f.write("<head>")
        f.write("<title>")
        f.write("爬虫数据")
        f.write("</title>")
        f.write("</head>")
        f.write("<body>")
        f.write("<table border=\"1\">")
        f.write("<thead>")
        f.write("<th>url</th>")
        f.write("<th>summary</th>")
        f.write("</thead>")
        f.write("<tbody>")
        for data in self.html_datas:
            f.write("<tr>")
            f.write("<td>")
            f.write("<a href=\""+data['url']+"\">")
            f.write((data['title'].encode('utf-8')))
            f.write("</a>")
            f.write("</td>")
            f.write("<td>" + data['summary'].encode('utf-8') + "</td>")
            f.write("</tr>")
        f.write("</tbody>")
        f.write("</table>")
        f.write("</body>")
        f.write("</html>")
        f.close()

    def collect_data(self, data_dict):
        if data_dict is None:
            return
        self.html_datas.append(data_dict)