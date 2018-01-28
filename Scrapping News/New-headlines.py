import requests
import re
from lxml import html
str = raw_input("Enter Tags\n").split(" ")
page = requests.get('https://timesofindia.indiatimes.com/')
html_content = html.fromstring(page.content)
news = html_content.xpath('//div/ul/li/a/text()')
news1 = html_content.xpath('//div/ul/li/a/span/text()')
news2 = html_content.xpath('//div/ul/li/span/a/text()')

tags = html_content.xpath('//div/ul/li/a/@pg')
tags1 = html_content.xpath('//div/ul/li/a/span/@pg')
tags2 = html_content.xpath('//div/ul/li/span/a/@pg')
for i in range(len(str)):
        print "News Containing " +str[i]+ " is"
        a = 0
        for j in range(len(tags)):
                if re.search(str[i], tags[j] , re.IGNORECASE):
                        if(j < len(news)):
                                print news[j]
                                a += 1
                elif (j < len(news) and re.search(str[i], news[j] , re.IGNORECASE)):
                        if(len(str[i]) < len(news[j])):
                                print news[j]
                                a += 1
        for j in range(len(tags1)):
                if re.search(str[i], tags1[j] , re.IGNORECASE):
                        if(j < len(news1)):
                                print news1[j]
                                a += 1
                elif (j < len(news1) and re.search(str[i], news1[j] , re.IGNORECASE)):
                        if(len(str[i]) < len(news1[j])):
                                print news1[j]
                                a += 1
        for j in range(len(tags2)):
                if re.search(str[i], tags2[j] , re.IGNORECASE):
                        if(j < len(news2)):
                                print news2[j]
                                a += 1
                elif (j < len(news2) and re.search(str[i], news2[j] , re.IGNORECASE)):
                        if(len(str[i]) < len(news2[j])):
                                print news2[j]
                                a += 1
        if(a == 0):
                print "No news Found For The Given Tag \n"
        else :
                print "\n"
