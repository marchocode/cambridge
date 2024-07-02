from utils import response_txt,response_byte
from define import Define
from element import Elememt
from bs4 import BeautifulSoup,Tag,NavigableString
import os
import json
from urllib.parse import urljoin
from const import DOMAIN

class Dictionary():

    def __init__(self, word):
        self.word=word
        self.url=f"{DOMAIN}/dictionary/english/{word}"
        self.elements=[]

    def __str__(self):
        return json.dumps(self.__dict__)

    def process(self):

        tag = self.load()
        self.cover_list(tag)
    
    def cover_list(self, diet: Tag) -> None:
        # block
        for item in diet.select("div.pr.entry-body__el"):
            ele = Elememt()
            ele.cover(item)
            self.elements.append(ele)

    def load(self) -> Tag:
        
        cache_file=f"{self.word}.html"

        if os.path.exists(cache_file):
            with open(cache_file,) as f:
                html=f.read()
        else:
            html = response_txt(self.request_url)
            with open(f"{self.word}.html", "w") as f:
                f.write(html)

        obj={"data-id":"cald4"}
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find(**obj)
    
    def cover_dict(self, dict:Tag) -> None:
        
        header=dict.select_one(".pos-header.dpos-h")
        sense_list = dict.select("div.pr.dsense")

        self.cover_none(header)
        self.cover_voice(header)

        for sense in sense_list:
            define = Define(sense)
            define.cover()


