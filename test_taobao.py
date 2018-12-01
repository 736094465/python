#coding:utf-8
import sys
import re
import requests
from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding("utf-8")

url = 'https://s.taobao.com/search'
payload = {'q': '麻城','s': '1','ie':'utf8'}  #字典传递url参数    
file = open('taobao_test.txt','w')

class myHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag=None
        self.strong=None

    def handle_starttag(self, tag, attrs):
        if tag=='div':
            for key,value in attrs:
                print "key=",key,"value=",value
                if key=='class' and value=='price g_price g_price-highlight':
                    print "find price tag"
                    self.flag='price'
        if tag=='strong':
            if self.price:
                self.strong='strong'

        def handle_endtag(self, tag, attrs):
            if tag=='strong':
                self.strong=None
                self.price=None
                
                def handle_data(self,data):
                    if self.strong:
                        print ("price:",data.decode('utf-8'))
                    
            


        

for k in range(0,2):        #100次，就是100个页的商品数据

    payload ['s'] = 44*k+1   #此处改变的url参数为s，s为1时第一页，s为45是第二页，89时第三页以此类推                          
    resp = requests.get(url, params = payload)
    print(resp.url)          #打印访问的网址
    resp.encoding = 'utf-8'  #设置编码
    #m=myHtmlParser()
    #m.feed(resp.text)
    #m.close()
    title = re.findall(r'"raw_title":"([^"]+)"',resp.text,re.I)  #正则保存所有raw_title的内容，这个是书名，下面是价格，地址
    price = re.findall(r'"view_price":"([^"]+)"',resp.text,re.I)
    #url = "test"#re.findall(r'"detail_url":"([^"]+)"',resp.text,re.I)   
    loc = re.findall(r'"item_loc":"([^"]+)"',resp.text,re.I)
    boss = re.findall(r'"nick":"([^"]+)"',resp.text,re.I)
    x = len(title)           #每一页商品的数量

    for i in range(0,x) :    #把列表的数据保存到文件中
        file.write(str(k*44+i+1)+'\n描述：'+title[i]+'\n'+'价格：'+price[i]+'\n'+'地址：'+loc[i]+'\n掌柜：'+boss[i]+'\n\n')


file.close()