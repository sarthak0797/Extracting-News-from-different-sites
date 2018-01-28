import requests
import re
from lxml import html
str = raw_input("Enter Tags\n").split(" ")
page = requests.get('https://timesofindia.indiatimes.com/')
html_content = html.fromstring(page.content)
news = html_content.xpath('//div/ul/li/a/text()')
news1 = html_content.xpath('//div/ul/li/a/span/text()')
news2 = html_content.xpath('//div/ul/li/span/a/text()')
for i in range(len(str)):
        print "Latest News Containing " +str[i]+ " is"
        a = 0
        for j in news:
                if re.search(str[i], j , re.IGNORECASE):
                        if(len(j) > len(str[i])):
                                print j
                                a += 1
        for j in news1:
                if re.search(str[i], j , re.IGNORECASE):
                        if(len(j) > len(str[i])):
                                print j
                                a += 1
        for j in news2:
                if re.search(str[i], j , re.IGNORECASE):
                        if(len(j) > len(str[i])):
                                print j
                                a += 1
        if(a == 0):
                print "No news Found For The Given Tag \n"
        else :
                print "\n"
