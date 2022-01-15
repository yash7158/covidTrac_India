#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 21:17:48 2021

@author: yashrajsingh
"""

import bs4
import requests

from prettytable import PrettyTable
x = PrettyTable()



from bs4 import BeautifulSoup as soup

my_url = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/India_medical_cases_by_state_and_union_territory'
res = requests.get(my_url)
page_html = res.text
page_soup = soup(page_html, 'html.parser')

ze=page_soup.findAll('table', class_='wikitable' )[0]

AN = ze.find_all('td')[0].getText()
AN_D = ze.find_all('td')[1].getText()
AN_R = ze.find_all('td')[2].getText()
AN_A = ze.find_all('td')[3].getText()

AP = ze.find_all('td')[4].getText()
AP_D = ze.find_all('td')[5].getText()
AP_R = ze.find_all('td')[6].getText()
AP_A = ze.find_all('td')[7].getText()

AR_P = ze.find_all('td')[8].getText()
AR_P_D = ze.find_all('td')[9].getText()
AR_P_R = ze.find_all('td')[10].getText()
AR_P_A = ze.find_all('td')[11].getText()

Assam = ze.find_all('td')[12].getText()
Assam_D = ze.find_all('td')[13].getText()
Assam_R = ze.find_all('td')[14].getText()
Assam_A = ze.find_all('td')[15].getText()


Bihar = ze.find_all('td')[16].getText()
Bihar_D = ze.find_all('td')[17].getText()
Bihar_R = ze.find_all('td')[18].getText()
Bihar_A = ze.find_all('td')[19].getText()

Chandigarh = ze.find_all('td')[20].getText()
Chandigarh_D = ze.find_all('td')[21].getText()
Chandigarh_R= ze.find_all('td')[22].getText()
Chandigarh_A = ze.find_all('td')[23].getText()


Chhattisgarh = ze.find_all('td')[24].getText()
Chhattisgarh_D = ze.find_all('td')[25].getText()
Chhattisgarh_R = ze.find_all('td')[26].getText()
Chhattisgarh_A = ze.find_all('td')[27].getText()

ddi= ze.find_all('td')[28].getText()
ddi_D = ze.find_all('td')[29].getText()
ddi_R = ze.find_all('td')[30].getText()
ddi_A = ze.find_all('td')[31].getText()

Delhi = ze.find_all('td')[32].getText()
Delhi_D = ze.find_all('td')[33].getText()
Delhi_R = ze.find_all('td')[34].getText()
Delhi_A = ze.find_all('td')[35].getText()


Goa = ze.find_all('td')[36].getText()
Goa_D = ze.find_all('td')[37].getText()
Goa_R = ze.find_all('td')[38].getText()
Goa_A = ze.find_all('td')[39].getText()

Gujrat = ze.find_all('td')[40].getText()
Gujrat_D = ze.find_all('td')[41].getText()
Gujrat_R = ze.find_all('td')[42].getText()
Gujrat_A = ze.find_all('td')[43].getText()

haryana = ze.find_all('td')[44].getText()
haryana_D = ze.find_all('td')[45].getText()
haryana_R = ze.find_all('td')[46].getText()
haryana_A = ze.find_all('td')[47].getText()


HP = ze.find_all('td')[48].getText()
HP_D = ze.find_all('td')[49].getText()
HP_R = ze.find_all('td')[50].getText()
HP_A = ze.find_all('td')[51].getText()


JK = ze.find_all('td')[52].getText()
JK_D = ze.find_all('td')[53].getText()
JK_R = ze.find_all('td')[54].getText()
JK_A = ze.find_all('td')[55].getText()

Jharkhand = ze.find_all('td')[56].getText()
Jharkhand_D = ze.find_all('td')[57].getText()
Jharkhand_R = ze.find_all('td')[58].getText()
Jharkhand_A = ze.find_all('td')[59].getText()

Karnataka = ze.find_all('td')[60].getText()
Karnataka_D = ze.find_all('td')[61].getText()
Karnataka_R = ze.find_all('td')[62].getText()
Karnataka_A = ze.find_all('td')[63].getText()

Kerala = ze.find_all('td')[64].getText()
Kerala_D = ze.find_all('td')[65].getText()
Kerala_R = ze.find_all('td')[66].getText()
Kerala_A = ze.find_all('td')[67].getText()


Ladakh = ze.find_all('td')[68].getText()
Ladakh = ze.find_all('td')[68].getText()
Ladakh_D = ze.find_all('td')[69].getText()
Ladakh_R = ze.find_all('td')[70].getText()
Ladakh_A = ze.find_all('td')[71].getText()

ld = ze.find_all('td')[72].getText()
ld_D = ze.find_all('td')[73].getText()
ld_R = ze.find_all('td')[74].getText()
ld_A = ze.find_all('td')[75].getText()

MP = ze.find_all('td')[76].getText()
MP_D = ze.find_all('td')[77].getText()
MP_R = ze.find_all('td')[78].getText()
MP_A = ze.find_all('td')[79].getText()


Maharashtra = ze.find_all('td')[80].getText()
Maharashtra_D = ze.find_all('td')[81].getText()
Maharashtra_R = ze.find_all('td')[82].getText()
Maharashtra_A = ze.find_all('td')[83].getText()

Manipur = ze.find_all('td')[84].getText()
Manipur_D = ze.find_all('td')[85].getText()
Manipur_R = ze.find_all('td')[86].getText()
Manipur_A = ze.find_all('td')[87].getText()

Meghalaya = ze.find_all('td')[88].getText()
Meghalaya_D = ze.find_all('td')[89].getText()
Meghalaya_R = ze.find_all('td')[90].getText()
Meghalaya_A = ze.find_all('td')[91].getText()

Mizoram = ze.find_all('td')[92].getText()
Mizoram_D = ze.find_all('td')[93].getText()
Mizoram_R = ze.find_all('td')[94].getText()
Mizoram_A = ze.find_all('td')[95].getText()

Nagaland = ze.find_all('td')[96].getText()
Nagaland_D = ze.find_all('td')[97].getText()
Nagaland_R = ze.find_all('td')[98].getText()
Nagaland_A = ze.find_all('td')[99].getText()

Odisha = ze.find_all('td')[100].getText()
Odisha_D = ze.find_all('td')[101].getText()
Odisha_R = ze.find_all('td')[102].getText()
Odisha_A = ze.find_all('td')[103].getText()

Puducherry= ze.find_all('td')[104].getText()
Puducherry_D = ze.find_all('td')[105].getText()
Puducherry_R = ze.find_all('td')[106].getText()
Puducherry_A = ze.find_all('td')[107].getText()

Punjab = ze.find_all('td')[108].getText()
Punjab_D = ze.find_all('td')[109].getText()
Punjab_R = ze.find_all('td')[110].getText()
Punjab_A = ze.find_all('td')[111].getText()

Rajasthan= ze.find_all('td')[112].getText()
Rajasthan_D = ze.find_all('td')[113].getText()
Rajasthan_R = ze.find_all('td')[114].getText()
Rajasthan_A = ze.find_all('td')[115].getText()

Sikkim= ze.find_all('td')[116].getText()
Sikkim_D = ze.find_all('td')[117].getText()
Sikkim_R = ze.find_all('td')[118].getText()
Sikkim_A = ze.find_all('td')[119].getText()

Tamil_Nadu = ze.find_all('td')[120].getText()
TN_D = ze.find_all('td')[121].getText()
TN_R = ze.find_all('td')[122].getText()
TN_A = ze.find_all('td')[123].getText()

Telangana = ze.find_all('td')[124].getText()
Telangana_D = ze.find_all('td')[125].getText()
Telangana_R = ze.find_all('td')[126].getText()
Telangana_A = ze.find_all('td')[127].getText()

Tripura = ze.find_all('td')[128].getText()
Tripura_D = ze.find_all('td')[129].getText()
Tripura_R = ze.find_all('td')[130].getText()
Tripura_A = ze.find_all('td')[131].getText()



UK = ze.find_all('td')[132].getText()
UK_D = ze.find_all('td')[133].getText()
UK_R = ze.find_all('td')[134].getText()
UK_A = ze.find_all('td')[135].getText()

UP = ze.find_all('td')[136].getText()
UP_D = ze.find_all('td')[137].getText()
UP_R = ze.find_all('td')[138].getText()
UP_A = ze.find_all('td')[139].getText()

WB = ze.find_all('td')[140].getText()
WB_D = ze.find_all('td')[141].getText()
WB_R = ze.find_all('td')[142].getText()
WB_A = ze.find_all('td')[143].getText()


x.field_names = ["S.No", "States/union teritory", "Total cases", "death","recovered","Active cases"]
x.add_row([1,"Andaman and nicobar inslands", AN, AN_D, AN_R,AN_A])
x.add_row([2,"Andra Pradesh", AP, AP_D, AP_R,AP_A])
x.add_row([3,"Arunachal Pradesh", AR_P, AR_P_D, AR_P_R,AR_P_A])
x.add_row([4,"Assam", Assam, Assam_D, Assam_R,Assam_A])
x.add_row([5,"Bihar", Bihar, Bihar_D, Bihar_R,Bihar_A])
x.add_row([6,"Chandigarh", Chandigarh, Chandigarh_D, Chandigarh_R,Chandigarh_A])
x.add_row([7,"Chhattisgarh", Chhattisgarh, Chhattisgarh_D, Chhattisgarh_R,Chhattisgarh_A])
x.add_row([8,"Dadra and Nagar Haveli and Daman and Diu", ddi, ddi_D, ddi_R,ddi_A])
x.add_row([9,"Delhi", Delhi, Delhi_D, Delhi_R,Delhi_A])
x.add_row([10,"Goa", Goa, Goa_D, Goa_R,Goa_A])
x.add_row([11,"Gujarat", Gujrat, Gujrat_D, Gujrat_R,Gujrat_A])
x.add_row([12,"Haryana", haryana, haryana_D, haryana_R,haryana_A])
x.add_row([13,"Himachal Pradesh", HP, HP_D, HP_R,HP_A])
x.add_row([14,"Jammu and Kashmir", JK, JK_D, JK_R,JK_A])
x.add_row([15,"Jharkhand", Jharkhand, Jharkhand_D, Jharkhand_R,Jharkhand_A])
x.add_row([16,"Karnataka", Karnataka, Karnataka_D, Karnataka_R,Karnataka_A])
x.add_row([17,"Kerala", Kerala, Kerala_D, Kerala_R,Kerala_A])

x.add_row([18,"Ladakh", Ladakh, Ladakh_D, Ladakh_R,Ladakh_A])
x.add_row([19,"Lakshadweep", ld, ld_D, ld_R,ld_A])
x.add_row([20,"Madhya Pradesh", MP, MP_D, MP_R,MP_A])
x.add_row([21,"Maharashtra", Maharashtra, Maharashtra_D, Maharashtra_R,Maharashtra_A])
x.add_row([22,"Manipur", Manipur, Manipur_D, Manipur_R,Manipur_A])
x.add_row([22,"Meghalaya", Meghalaya, Meghalaya_D, Meghalaya_R,Meghalaya_A])
x.add_row([24,"Mizoram", Mizoram, Mizoram_D, Mizoram_R,Mizoram_A])
x.add_row([25,"Nagaland", Nagaland, Nagaland_D, Nagaland_R,Nagaland_A])

x.add_row([25,"Odisha", Odisha, Odisha_D, Odisha_R,Odisha_A])
x.add_row([26,"Puducherry", Puducherry, Puducherry_D, Puducherry_R,Puducherry_A])
x.add_row([27,"Punjab", Punjab, Punjab_D, Punjab_R,Punjab_A])
x.add_row([28,"Rajasthan", Rajasthan, Rajasthan_D, Rajasthan_R,Rajasthan_A])
x.add_row([29,"Andaman and nicobar inslands", AN, AN_D, AN_R,AN_A])
x.add_row([30,"Sikkim",Sikkim, Sikkim_D, Sikkim_R,Sikkim_A])
x.add_row([31,"Tamil Nadu", Tamil_Nadu, TN_D, TN_R,TN_A])
x.add_row([32,"Telangana", Telangana, Telangana_D, Telangana_R,Telangana_A])
x.add_row([33,"Tripura", Tripura, Tripura_D, Tripura_R,Tripura_A])
x.add_row([34,"Uttarakhand", UK, UK_D, UK_R,UK_A])
x.add_row([35,"UTTER PRADESH", UP, UP_D, UP_R,UP_A])
x.add_row([36,"West Bengal", WB, WB_D, WB_R,WB_A])
print(x)
