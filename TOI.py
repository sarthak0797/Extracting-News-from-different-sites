import requests
import re
from lxml import html

def get_news(str,keys):

    page = requests.get('https://timesofindia.indiatimes.com/')

    html_content = html.fromstring(page.content)

    news = html_content.xpath('//div/ul/li/a/text()')

    news1 = html_content.xpath('//div/ul/li/a/span/text()')

    news2 = html_content.xpath('//div/ul/li/span/a/text()')


    tags = html_content.xpath('//div/ul/li/a/@pg')

    tags1 = html_content.xpath('//div/ul/li/a/span/@pg')

    tags2 = html_content.xpath('//div/ul/li/span/a/@pg')

    for i in range(len(keys)):
        
        for j in range(len(tags)):

                if re.search(keys[i], tags[j] , re.IGNORECASE):

                        if(j < len(news) and len(news[j]) > 9):

                                str.append(news[j])

                elif (j < len(news) and re.search(keys[i], news[j] , re.IGNORECASE)):

                        if(len(keys[i]) < len(news[j])):

                                str.append(news[j])

        for j in range(len(tags1)):

                if re.search(keys[i], tags1[j] , re.IGNORECASE):

                        if(j < len(news1)):

                                str.append(news[j])

                elif (j < len(news1) and re.search(keys[i], news1[j] , re.IGNORECASE)):

                        if(len(keys[i]) < len(news1[j])):

                                str.append(news[j])

        for j in range(len(tags2)):

                if re.search(keys[i], tags2[j] , re.IGNORECASE):

                        if(j < len(news2)):

                                str.append(news[j])

                elif (j < len(news2) and re.search(keys[i], news2[j] , re.IGNORECASE)):

                        if(len(str[i]) < len(news2[j])):

                                str.append(news[j])
    return str
