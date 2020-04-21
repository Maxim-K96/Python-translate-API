#!/usr/bin/env python
# -*- encoding: utf-8 -*- 

import sys
import requests
import simplejson as json

class Translate:
    def __init__(self, lang, doc): 
        self.langvige = lang,
        self.doc = doc,
        self.user_agent = {'User-Agent': '<Your User-Agent>'}
    def translate_handler(self):
        for i in self.doc: word = i
        word = ' '.join(word)
        self.langvige = ' '.join(self.langvige)
        try:
            if self.langvige  == 'ru':
                req = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?lang=en-ru&key=<You API_key>&format=plain&options=1&text=%s' % word, headers=self.user_agent) 
            elif self.langvige == 'en':
                req = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key=<You API_key>&lang=ru-en&format=plain&options=1&text=%s' % word, headers=self.user_agent)
            else: 
                print('Available languages: en, ru')
                return
        except requests.HTTPError as err:  # Исправить
            print ('http error') 
            print('Response is: {content}'.format(content=err))
        req.json()
        if req.status_code != 200: 
            print ( req.status_code + ': ' + str(req))
        elif req.status_code == 200:
            translate_value = req.json()
            print(' '.join(translate_value['text']))
        else: 
            print('unknow error >_<')

def main():
	translate = Translate(sys.argv[1], sys.argv[2:]) # Передача нескольких аргументов
	translate.translate_handler()


if __name__== "__main__":
	main()
