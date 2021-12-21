import json
import xml.etree.ElementTree as elem_tree
from urllib.request import urlopen

def save_data(filename, data):
	with open(filename, 'w', encoding='utf-8') as file:
		json.dump(data, fp=file, ensure_ascii=False, indent=4)

root = elem_tree.fromstring(urlopen('https://lenta.ru/rss').read().decode('utf8'))

# Получаем только нужные нам данные (заголовки и даты публикаций)
data = []
for parent in root.findall(r'./channel/item'):
    date = parent.findtext('pubDate')
    title = parent.findtext('title')
    data.append({'pubDate': date, 'title': title})
save_data('news.json', data)

# Получаем все теги и их содержимое
data = []
for parent in root.findall(r'./channel/item'):
    dictionary = {}
    for tag in parent:
        dictionary[tag.tag] = tag.text
    data.append(dictionary)
save_data('news2.json', data)