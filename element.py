from bs4 import Tag
from urllib.parse import urljoin
from const import DOMAIN
from define import Define

class Elememt():

    def __init__(self):
        self.pos = None
        self.us_voice = None
        self.uk_voice = None
        self.defines = []

    def cover(self, dict: Tag) -> None:

        header=dict.select_one(".pos-header.dpos-h")
        sense_list = dict.select("div.pr.dsense")
        
        self.cover_none(header)
        self.cover_voice(header)

        for sense in sense_list:
            define = Define(sense)
            define.cover()


    def cover_none(self, dict:Tag) -> None:
        self.pos = dict.select_one('span.pos.dpos').text   

    def cover_voice(self, dict:Tag) -> None:

        uk_source = dict.select_one(".uk.dpron-i source[type='audio/mpeg']")
        us_source = dict.select_one(".us.dpron-i source[type='audio/mpeg']")

        self.us_voice = urljoin(DOMAIN,us_source['src'])
        self.uk_voice = urljoin(DOMAIN,uk_source['src'])