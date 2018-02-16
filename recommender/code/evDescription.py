#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from pprint import pprint
import requests
import codecs


def buscaDescription(Id):
    senha = 'EAACEdEose0cBAHeRDXsqs7spKGIFI4EMWlA56kEA1ZAmuAUc28rC1YjH1ZAZCoZBc79xiXIDVpcFrsZAbWNfy3Izl6RrEov9pBOxctwyYYHjJUORpjTnIq1QDjrerlaAnubpcu5lICTY7IWUepWY4G7sVh6IgbPpBkqdaMPoRdF9P4tHphNYOZBZAruKJrFI8stssPgOuHemQZDZD'
    desc = ""
    cep = ""
    inicio = ""
    idLocal = ""
    idEvento = ""


    r = requests.get("https://graph.facebook.com/v2.10/"+Id+"?fields=id,description,start_time,place&access_token="+senha)


    data = r.json()
    try:
        desc = data['description']
    except:
        pass
    desc =  desc.replace("\n","")
    desc = desc.replace("\"", "")
    desc = desc.replace(",", "")
    #print desc
    try:
        cep = data['place']['location']['zip']
    except:
        pass
    try:
        inicio = data['start_time']
    except:
        pass

    try:
        idLocal = data['place']['id']
    except:
        pass

    try:
        idEvento = data['id']
    except:
        pass
    evInfo = idEvento + "," +  idLocal + "," +  inicio + "," + cep  + "," + desc
    print evInfo
    return evInfo





Id = open("../idEeventos", "r")

ev = open("evInfo.csv", "w")


for cada in Id:
    buscaDescription(cada)





"""
for cada in listaId:
cada = "117077292303825"
buscaDescription(cada)
"""


'''
    count = 0
    while (count < tam):
        dataJ = data['interested']['data'][count]
        dataset.write(data['id']+","+data['start_time']+",")
        count = count +1
        dataA = dataJ['interested']
        dataA = dataA['data']
        tam2 = len(dataA)
        print tam2
        count2 = 0

        while (count2 < tam2):
            dataset.write(dataA[count2]['id']+",")
            count2 = count2 +1
        dataset.write('\n')
'''
