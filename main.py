from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.request import urlopen
import re
from collections import Counter
#html = urlopen('https://ru.wikipedia.org/wiki/Python').read().decode('utf-8')

# convert html to string

#s = str(html)

# let's separate text from tags, remove everything bounded by '<' and '>', find C++.
#
# cplus = tuple(re.finditer(r'[Cc]\+\+]|[Cc]\+\+|[С]и\+\+', html))
# print(f'C++ {len(cplus)}')

# h_task = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html ').read().decode('utf-8')

# Регулярное выражение '<code>(.*?)</code>' означает,
# что сюда должно попадать любое выражение, которое начинается
# на <code>, заканчивается на</code>, а в середине между ними может
# быть любое количество любых символов, или не быть вовсе(.*), знак ?
# нужен для отключения "жадности" (есть такая фича в регулярных выражениях).
# Скобки нужны, чтобы функция findall() из модуля re из всего выражения
# взяла только то что в скобках, она делает
# список из всех этих встречающихся выражений.

# regexpr = '<code>(.*?)</code>'
#
# l = re.findall(regexpr, h_task)
# c = Counter(l)
# print(c)


# html = urlopen('https://ru.wikipedia.org/wiki/Python').read().decode('utf-8')



# let's create variable with url, number of reviews we will take equal to 100 (and we will point
# it in GET request to website, we will parse 10 first pages (more recent reviews)

number_of_pages = 11
reviews_on_page = 100
url = 'https://www.airlinequality.com/airline-reviews/british-airways' # this is a base url for scraping

# we will collect parsed data to this list
reviews = []

for i in range(1, number_of_pages):

    # this is GET request to website - TEMPLATE
    get_url = f'{url}/page/{i}/?sortby=post_date%3ADesc&pagesize={reviews_on_page}'

    # that is how we get data from the website - we get text
    response_from_website = requests.get(get_url)

    # now it's time to get content we interested from the website
    parsed_content = BeautifulSoup(response_from_website.content, 'html.parser')
    for i in parsed_content.find_all('div', {"class": "text_content"}):
        reviews.append(i.get_text())

df = pd.DataFrame()
df['reviews'] = reviews


df.to_csv('reviews_dataset.csv')
# let's create GET request

# get = requests.get(url)
# # let's parse our get with help of beautifulsoup
#
# parse_get = BeautifulSoup(get.text, "html.parser")
# print(parse_get) # we see 200 - everything is OK.

