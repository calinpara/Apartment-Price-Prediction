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
lst_var_17 = list()
lst_var_18 = list()
lst_var_19 = list()


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
        location = _soup.find(class_='first active').get('rel')
        loc_string = ''.join([str(item) for item in location])
        zone_string = _soup.find(class_='col-lg-9 col-md-9 col-sm-9 col-xs-12').get_text()

        def findnth(the_string, substring, n):
            parts = the_string.split(substring, n + 1)
            if len(parts) <= n + 1:
                return -1
            return len(the_string) - len(parts[-1]) - len(substring)

        indx_1 = findnth(loc_string, '/', 10)
        indx_2 = findnth(loc_string, '/', 12)
        indx_3 = findnth(zone_string, 'Hartă', 0)

        lat_string = str()
        if 'lat' in loc_string:
            index = loc_string.find('lat')
            string = 'Latitudine:'
            lat_string += loc_string[index + 4:indx_1]
            lat_string = '{0}{1}'.format(string, lat_string)

        lon_string = str()
        if 'lon' in loc_string:
            index = loc_string.find('lon')
            string = 'Longitudine:'
            lon_string += loc_string[index + 4:indx_2]
            lon_string = '{0}{1}'.format(string, lon_string)

        zona_string = str()
        if 'zona' in zone_string:
            index = zone_string.find('zona')
            string = 'Zona:'
            zona_string += zone_string[index + 5:indx_3 - 2]
            zona_string = '{0}{1}'.format(string, zona_string)

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

        new_lst_1 = list()
        for row in each_row_lst_1:
            text_row_1 = row.get_text()
            if 'mp' in text_row_1:
                index = new_price.find('mp')
                text_row_1 = text_row_1[:index - 1]
            new_lst_1.append(text_row_1)

        new_lst_2 = list()
        for row in each_row_lst_2:
            text_row_2 = row.get_text()
            new_lst_2.append(text_row_2)

        full_lst = new_lst_1 + new_lst_2
        full_lst.append(lat_string)
        full_lst.append(lon_string)
        full_lst.append(zona_string)
        full_lst.append(price_string)

        print(full_lst)

        tup = ('Nr. camere', 'Suprafaţă utilă:','Suprafaţă utilă totală', 'Suprafaţă construită','Compartimentare',
               'Confort', 'Etaj', 'Nr. bucătării','Nr. băi','An construcţie', 'Structură rezistenţă', 'Tip imobil',
               'Regim înălţime', 'Nr. garaje', 'Nr. locuri parcare', 'Nr. balcoane', 'Latitudine', 'Longitudine',
               'Zona', 'Pret')

        lst_var0 = [item if tup[0] in item else 'NaN' for item in full_lst]
        lst_var1 = [item if tup[1] in item else 'NaN' for item in full_lst]
        lst_var2 = [item if tup[2] in item else 'NaN' for item in full_lst]
        lst_var3 = [item if tup[3] in item else 'NaN' for item in full_lst]
        lst_var4 = [item if tup[4] in item else 'NaN' for item in full_lst]
        lst_var5 = [item if tup[5] in item else 'NaN' for item in full_lst]
        lst_var6 = [item if tup[6] in item else 'NaN' for item in full_lst]
        lst_var7 = [item if tup[7] in item else 'NaN' for item in full_lst]
        lst_var8 = [item if tup[8] in item else 'NaN' for item in full_lst]
        lst_var9 = [item if tup[9] in item else 'NaN' for item in full_lst]
        lst_var10 = [item if tup[10] in item else 'NaN' for item in full_lst]
        lst_var11 = [item if tup[11] in item else 'NaN' for item in full_lst]
        lst_var12 = [item if tup[12] in item else 'NaN' for item in full_lst]
        lst_var13 = [item if tup[13] in item else 'NaN' for item in full_lst]
        lst_var14 = [item if tup[14] in item else 'NaN' for item in full_lst]
        lst_var15 = [item if tup[15] in item else 'NaN' for item in full_lst]
        lst_var16 = [item if tup[16] in item else 'NaN' for item in full_lst]
        lst_var17 = [item if tup[17] in item else 'NaN' for item in full_lst]
        lst_var18 = [item if tup[18] in item else 'NaN' for item in full_lst]
        lst_var19 = [item if tup[19] in item else 'NaN' for item in full_lst]

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
        lst_var_17.append(lst_var17[function_2(lst_var17)])
        lst_var_18.append(lst_var18[function_2(lst_var18)])
        lst_var_19.append(lst_var19[function_2(lst_var19)])

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
    'Latitudine': lst_var_16,
    'Longitudine': lst_var_17,
    'Zona': lst_var_18,
    'Pret': lst_var_19,
})

print(df)

df.to_csv('apartamente2.csv')
