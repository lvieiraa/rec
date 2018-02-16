#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
from pprint import pprint
import requests
import json
import codecs


def buscaEventos(local):
    print local

    arq_saida = local
    dataset = open("../listaAntiga/noReply/"+arq_saida, 'a')

    senha = 'EAACEdEose0cBAOoOdUWuzw71j3CPiPpZCnZBKBwRc4pGBuW8ln2vgH2DQBvLwsIf6kz2fAVma25AZBpfTTZCW8kAJzfNkVkicps8BZArn98vYhjS5YqOVDHsrClZArLZA9W3LrixhmyiVRy3gQAGCnFdtItsCLfCXZAMHrT7DNROfORZArAYgzkq5QKZCO5GBKipVae4ChG1zc8wZDZD'

    try:
        r = requests.get("https://graph.facebook.com/v2.10/"+local+"?fields=start_time,noreply.limit(50000){id}&access_token="+senha)
        dados = r.text
        data = json.loads(dados)
        #pprint (data)
        tam = len(data['noreply']['data'])
        count2 = 0
        dataset.write(data['id']+","+data['start_time']+",")
        while (count2 < tam):
            dataset.write(data['noreply']['data'][count2]['id']+",")
            count2 = count2 +1
        dataset.write('\n')
    except:
        pass

Id = open("../idEeventos", "r")

for cada in Id:
    buscaEventos(cada)
