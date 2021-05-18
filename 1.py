from main import category, HOST
from bs4 import BeautifulSoup as bs
import requests
import csv

def in_catalog_page():
    ff = 'https://www.stout.ru/catalog/aksessuary-i-komplektuyushchie'
    #ff = 'https://www.stout.ru/catalog/vodonagrevateli-0'
    page_item = ''
    response_page = requests.get(ff)
    page = bs(response_page.text, 'lxml')
    bb = page.find_all('div', class_='field field-name-node-link field-type-ds field-label-hidden')
    for p_item in bb:
        pg = p_item.find('a').get('href')
        page_item += f"{HOST}{pg},"
    len_page_item = len(page_item.split(','))
    for i in range(len_page_item):
        print(page_item.split(',')[i])
        if page_item.split(',')[i] != "":
            page_item_path = requests.get(page_item.split(',')[i])
            page_item_cat = bs(page_item_path.text, 'lxml')
            item_title = page_item_cat.find('h1', class_='page-header')
            item_artcles = page_item_cat.find('div', class_='field-item even', itemprop='sku')
            item_price_up_level = page_item_cat.find('div', class_='field field-name-commerce-price field-type-commerce-price field-label-inline clearfix clearfix')
            item_content = page_item_cat.find('div', class_='field-content')
            print(item_content.text)
            # print("Название: {}".format(item_title.text))
            # print("Артикул: {}".format(item_artcles.text))
            # print(item_price_up_level.text)

        




print(in_catalog_page())

                 # bb = page.find_all('div', class_='field field-name-title-microdata field-type-ds field-label-hidden')
                # pr = page.find_all('div', itemprop="offers")
                # art = page.find_all('div', class_='field-item even', itemprop="sku")
                # for bbs in bb:
                #     if bbs.text not in num_page_cat:
                #         for prs in pr:
                #             for atrs in art:
                #                 print(f'Название: {bbs.text.strip()}\n'
                #                       f'Цена: {prs.text}\n'
                #                       f'Артикул: {atrs.text}\n'
                #                       f'==========================')





# dict_item = {}
# for i in range(len)


# with open('ex.csv', 'w', newline='') as file:
#     columns = ["Link to goods"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#     writer.writerows(dict_item)




