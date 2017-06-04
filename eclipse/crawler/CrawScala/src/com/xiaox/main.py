'''
Created on 2017年6月3日

@author: XiaoX
'''
from bs4 import BeautifulSoup
import urllib.request
import os

class CrawScala(object):
    def __init__(self, url):
        self.t1 = {}
        self.t2 = {}
        self.t3 = {}
        self.soup = BeautifulSoup(urllib.request.urlopen(url).read())
        
    def getLinks(self):
        page = self.soup.find('div', class_="bottom").find('div', class_="span10")
        title1 = page.find_all('div', class_="page-header-index")
        title1_name = []  # 存储一级目录的名字
        for name in title1:
            title1_name.append(name.find("h2").string)
        title2 = page.find_all("ul", recursive=False)
        for x in range(len(title2)):
            title2_name = []  # 存储二级目录的名字
            for y in title2[x].find_all("li", recursive=False):
                str = y.contents[0]
                if(str.find("href") != -1):  # 二级标题是链接
                    self.t2[str.string.strip()] = str['href']
                    # print("二级标题：%s %s" % (title2[x].get_text(),title2[x].find('a')['href']))
                else:  # 二级目录不是链接
                    self.t2[str.string.strip()] = ''
                    str1 = y.contents[1]
                    title3 = {}
                    if str1 is not None:  # 包含三级目录
                        for z in str1.find_all('a'):
                            title3[z.string] = z['href']
                            # print("%s---->%s" %(z.string,z['href']))
                    if title3 is not None:
                        self.t3[str.string.strip() + "_title3"] = title3
                    # print("二级标题：%s" %(title2[x].contents[0]))
                title2_name.append(str.string.strip())  # 保存二级目录名字
            self.t1[title1_name[x]] = title2_name  # 将二级目录加入对应的三级目录中
    def mkDownloadDir(self, local_path):
        for title1 in self.t1.items():
            os.makedirs(local_path + "\\" + title1[0])
            for title2 in title1[1]:
                if self.t3.get(title2 + "_title3") is not None:
                    os.makedirs(local_path + "\\" + title1[0] + "\\" + title2)

    
    def mkDownloadLinks(self):
        base_path = "http://docs.scala-lang.org"
        linkMap = {}
        for title1 in self.t1.items():
            for title2 in title1[1]:
                if self.t3.get(title2 + "_title3") is not None:
                    for title3 in self.t3.get(title2 + "_title3").items():
                        pass
                        linkMap[title1[0] + "\\" + title2 + "\\" + title3[0] + ".html"] = base_path + title3[1]
                else:
                    linkMap[title1[0] + "\\" + title2 + ".html"] = base_path + self.t2.get(title2)
        return linkMap       

    
    def downloadLinks(self, local_path,linkMap):
        for x in linkMap.items():
            html_cont = self.download(x[1])
            self.output_html(local_path +"\\"+ x[0], html_cont)
            
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        return response.read()
    def output_html(self, path, content):
        fout = open(path, 'w', encoding='utf-8')
        fout.write(content.decode())
        fout.close()
if __name__ == "__main__":
    root_url = "http://docs.scala-lang.org/zh-cn/overviews/"
    local_path = "d:\\test"
    object_spider = CrawScala(root_url)
    object_spider.getLinks()  # 获取下载链接
    object_spider.mkDownloadDir(local_path)  # 创建目录
    linkMap = object_spider.mkDownloadLinks()  # 构造下载链接
    object_spider.downloadLinks(local_path,linkMap)  # 下载
