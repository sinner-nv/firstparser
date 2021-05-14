from main import category, HOST
from bs4 import BeautifulSoup as bs
import requests
import csv

def in_catalog_page():
    #num_page_cat = ''
    page_item = ''
    ff = 'https://www.stout.ru/catalog/aksessuary-i-komplektuyushchie'
    for page_c in range(len(category())):
        for i in range(1):
            #v_url = f'{category()[page_c]}?page={i}'
            v_url = f'{ff}?page={i}'
            response_page = requests.get(v_url)
            page = bs(response_page.text, 'lxml')
            # a = page.find_all('li', class_='next')
            # if a != []:
            bb = page.find_all('div', class_='field field-name-node-link field-type-ds field-label-hidden')
            for p_item in bb:
               pg = p_item.find('a').get('href')
               page_item += f"{HOST}{pg},"

    return page_item.split(',')

print(in_catalog_page(),end='\n')

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




