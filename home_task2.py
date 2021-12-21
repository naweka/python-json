from urllib.request import urlopen
from json import loads
from itertools import groupby

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))['query']['pages']['192203']['revisions']
dates_list = []

for date, counts in groupby(data, lambda x: x['timestamp'].split('T')[0]):
    dates_list.append([date, len(list(counts))])

print(f'Предполагаемая дата смерти: {sorted(dates_list, key=lambda x: x[1], reverse=True)[0][0]}')