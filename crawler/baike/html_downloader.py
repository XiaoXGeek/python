'''
Created on 2017年4月28日

@author: XiaoX
'''
import urllib.request
#from pip._vendor.requests.packages import urllib3


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        
        if response.getcode()!=200:
            return None
        return response.read()
        
    
    



