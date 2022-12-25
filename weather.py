import requests
from bs4 import BeautifulSoup as bs

with open('URL_IMPORTANT.txt','r') as f:
	url = f.read()
response = requests.get(url)
soup = bs(response.text, "lxml")


_soup1 = soup.find('div', 'temp fact__temp fact__temp_size_s')
better_soup = (str(_soup1.text) + '°')
print('\n Температура сейчас:', better_soup)

feel = soup.find('div', 'term term_orient_h fact__feels-like')
feel1 = feel.find('span')
print(f' Ощущается как {feel1.text}°\n')

water = soup.find('div', 'maps-widget-nowcast card content__brief')
water2 = water.find('p')
print('',water2.text)

how = soup.find('div', 'link__condition day-anchor i-bem')
print('',how.text)

#print('\n' + str(response))


input('\n Нажмите ENTER для выхода')