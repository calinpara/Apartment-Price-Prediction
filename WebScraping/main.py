import requests
from bs4 import BeautifulSoup
import pandas as pd


flag = True
global price

lst_var_0 = list()
lst_var_1 = list()
lst_var_2 = list()
lst_var_3 = list()
lst_var_4 = list()
lst_var_5 = list()
lst_var_6 = list()
lst_var_7 = list()
lst_var_8 = list()
lst_var_9 = list()
lst_var_10 = list()
lst_var_11 = list()
lst_var_12 = list()
lst_var_13 = list()
lst_var_14 = list()
lst_var_15 = list()
lst_var_16 = list()


# FUNCTION THAT RETURNS THE LIST OF NEEDED CHARACTERISTICS
def function(string_links):
    global flag, price
    _page = requests.get(string_links)
    _soup = BeautifulSoup(_page.content, 'html.parser')

    try:
        price = _soup.find(class_='pret first blue').get_text()
    except AttributeError:
        print("Pretul pentru anuntul asta nu exista!")
        flag = False

    if flag:
        columns_lst = _soup.find_all(class_='col-lg-6 col-md-6 col-sm-6')
        column_1 = columns_lst[0].find(class_='lista-tabelara')
        each_row_lst_1 = column_1.find_all('li')
        column_2 = columns_lst[1].find(class_='lista-tabelara')
        each_row_lst_2 = column_2.find_all('li')

        price_string = 'Pret:'
        new_price_1 = price.replace('EUR + TVA', '')
        new_price = new_price_1.replace('EUR', '')

        new_price_2 = price.replace('RON + TVA', '')
        new_price_3 = new_price_2.replace('RON', '')

        for string in price:
            if string == 'D':
                index_1 = new_price.find('D')
                price_string += new_price[index_1 + 1:]
                break

            elif string == 'E':
                index_1 = new_price_3.find('E')
                price_string += new_price_3[:index_1]
                break

        new_lst_1 = []
        for row in each_row_lst_1:
            text_row_1 = row.get_text()
            if 'mp' in text_row_1:
                index = new_price.find('mp')
                text_row_1 = text_row_1[:index - 1]
            new_lst_1.append(text_row_1)

        new_lst_2 = []
        for row in each_row_lst_2:
            text_row_2 = row.get_text()
            new_lst_2.append(text_row_2)

        full_lst = new_lst_1 + new_lst_2

        full_lst.append(price_string)

        print(full_lst)

        var0 = 'Nr. camere'
        var1 = 'Suprafaţă utilă:'
        var2 = 'Suprafaţă utilă totală'
        var3 = 'Suprafaţă construită'
        var4 = 'Compartimentare'
        var5 = 'Confort'
        var6 = 'Etaj'
        var7 = 'Nr. bucătării'
        var8 = 'Nr. băi'
        var9 = 'An construcţie'
        var10 = 'Structură rezistenţă'
        var11 = 'Tip imobil'
        var12 = 'Regim înălţime'
        var13 = 'Nr. garaje'
        var14 = 'Nr. locuri parcare'
        var15 = 'Nr. balcoane'
        var16 = 'Pret'

        lst_var0 = [item if var0 in item else 'NaN' for item in full_lst]
        lst_var1 = [item if var1 in item else 'NaN' for item in full_lst]
        lst_var2 = [item if var2 in item else 'NaN' for item in full_lst]
        lst_var3 = [item if var3 in item else 'NaN' for item in full_lst]
        lst_var4 = [item if var4 in item else 'NaN' for item in full_lst]
        lst_var5 = [item if var5 in item else 'NaN' for item in full_lst]
        lst_var6 = [item if var6 in item else 'NaN' for item in full_lst]
        lst_var7 = [item if var7 in item else 'NaN' for item in full_lst]
        lst_var8 = [item if var8 in item else 'NaN' for item in full_lst]
        lst_var9 = [item if var9 in item else 'NaN' for item in full_lst]
        lst_var10 = [item if var10 in item else 'NaN' for item in full_lst]
        lst_var11 = [item if var11 in item else 'NaN' for item in full_lst]
        lst_var12 = [item if var12 in item else 'NaN' for item in full_lst]
        lst_var13 = [item if var13 in item else 'NaN' for item in full_lst]
        lst_var14 = [item if var14 in item else 'NaN' for item in full_lst]
        lst_var15 = [item if var15 in item else 'NaN' for item in full_lst]
        lst_var16 = [item if var16 in item else 'NaN' for item in full_lst]

        def function_2(lista):
            indx = 0
            for itm in lista:
                if itm != 'NaN':
                    indx = lista.index(itm)
                    new_itm = itm.split(':')
                    new_itm = new_itm[1]
                    lista[indx] = new_itm
                    indx = lista.index(new_itm)
            return indx

        lst_var_0.append(lst_var0[function_2(lst_var0)])
        lst_var_1.append(lst_var1[function_2(lst_var1)])
        lst_var_2.append(lst_var2[function_2(lst_var2)])
        lst_var_3.append(lst_var3[function_2(lst_var3)])
        lst_var_4.append(lst_var4[function_2(lst_var4)])
        lst_var_5.append(lst_var5[function_2(lst_var5)])
        lst_var_6.append(lst_var6[function_2(lst_var6)])
        lst_var_7.append(lst_var7[function_2(lst_var7)])
        lst_var_8.append(lst_var8[function_2(lst_var8)])
        lst_var_9.append(lst_var9[function_2(lst_var9)])
        lst_var_10.append(lst_var10[function_2(lst_var10)])
        lst_var_11.append(lst_var11[function_2(lst_var11)])
        lst_var_12.append(lst_var12[function_2(lst_var12)])
        lst_var_13.append(lst_var13[function_2(lst_var13)])
        lst_var_14.append(lst_var14[function_2(lst_var14)])
        lst_var_15.append(lst_var15[function_2(lst_var15)])
        lst_var_16.append(lst_var16[function_2(lst_var16)])

    flag = True


link = 'https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov?id=82493726&pagina='

# A LIST OF PAGES URL'S
page_lst = []
NUM_PAGES = 334
for num in range(1, NUM_PAGES + 1):
    link_string = link + str(num)
    page_lst.append(link_string)

# LOOPING THROUGH THE LIST OF PAGES URL'S AND CREATING LISTS OF ACTUAL LINKS INSIDE PAGES
variable = ''
for pg in page_lst:
    print(pg)
    page = requests.get(pg)
    soup = BeautifulSoup(page.content, 'html.parser')
    images = soup.find_all(class_='img-block')
    links_lst = [link.get('href') for link in soup.find_all(class_='img-block')]

    for lnk in links_lst:
        function(lnk)

df = pd.DataFrame({
    'Nr camere': lst_var_0,
    'Suprafata utila': lst_var_1,
    'Suprafata utila totala': lst_var_2,
    'Suprafata construita': lst_var_3,
    'Compartimentare': lst_var_4,
    'Confort': lst_var_5,
    'Etaj': lst_var_6,
    'Nr. bucatarii': lst_var_7,
    'Nr. bai': lst_var_8,
    'An constructie': lst_var_9,
    'Structura rezistenta': lst_var_10,
    'Tip imobil': lst_var_11,
    'Regim inaltime': lst_var_12,
    'Nr. garaje': lst_var_13,
    'Nr. locuri parcare': lst_var_14,
    'Nr. balcoane': lst_var_15,
    'Pret': lst_var_16,
})

print(df)

df.to_csv('apartamente.csv')
