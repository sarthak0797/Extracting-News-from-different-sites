import requests
import re
from lxml import html
def get_news(str,keys1):

    page = requests.get('http://www.bbc.com/news')

    html_content = html.fromstring(page.content)

    news = html_content.xpath('//div/div/a/h3/text()')

    for j in range(len(news)):

            if re.search(keys1, news[j] , re.IGNORECASE) :

                    if(len(keys1) < len(news[j]) and len(news[j]) > 20):

                            str.append(news[j])

    return str

