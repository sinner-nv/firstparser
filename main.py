from bs4 import BeautifulSoup as bs
import requests


HOST = 'https://www.stout.ru/'
response = requests.get(HOST)
soup = bs(response.text, 'lxml')


def category():
    dontentr = ['Контакты',
            'О бренде',
            'Карта сайта',
            'Где купить',
            'Обратная связь',
            'Выполненные объекты',
            'Статьи']
    category = ''
    q = soup.find_all('li', class_='leaf')
    for i, cat in enumerate(q, start=1):
        if cat.text not in dontentr:
            category += f"{HOST}{cat.find('a').get('href')},"
    return category.split(',')

def in_catalog_page():
    num_page_cat = ''
    for page_c in range(len(category())):
        for i in range(0, 50):
            v_url = f'{category()[page_c]}?page={i}'
            response_page = requests.get(v_url)
            page = bs(response_page.text, 'lxml')
            a = page.find_all('li', class_='next')
            if a != []:
                bb = page.find_all('div', class_='field field-name-title-microdata field-type-ds field-label-hidden')
                pr = page.find_all('div', itemprop="offers")
                art = page.find_all('div', class_='field-item even', itemprop="sku")
                for bbs in bb:
                    if bbs.text not in num_page_cat:
                        for prs in pr:
                            for atrs in art:
                                print(f'Название: {bbs.text.strip()}\n'
                                      f'Цена: {prs.text}\n'
                                      f'Артикул: {atrs.text}\n'
                                      f'==========================')

in_catalog_page()