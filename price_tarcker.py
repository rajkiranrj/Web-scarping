import requests as r
import bs4

base_url = 'https://www.dollartree.com/'

url = 'https://www.dollartree.com/colorful-plastic-spray-bottles-10oz/334194'

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

base_response = r.get(base_url)

cookies = base_response.cookies

prod_response = r.get(url, headers=headers, cookies=cookies)

soup = bs4.BeautifulSoup(prod_response.text, features='lxml')

price_lines = soup.findAll(class_='a-price-whole')

print(price_lines)

