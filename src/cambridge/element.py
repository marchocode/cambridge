from bs4 import Tag
from urllib.parse import urljoin
from .const import DOMAIN
from .define import Define

class Elememt():

    def __init__(self):
        self.pos = None
        self.us_voice = None
        self.uk_voice = None
        self.us_pron = None
        self.uk_pron = None
        self.defines = []

    def cover(self, tag: Tag) -> dict:

        header=tag.select_one("div.pos-header.dpos-h")
        sense_list = tag.select("div.pr.dsense")
        
        self.cover_none(header)
        self.cover_voice(header)

        for sense in sense_list:
            define = Define()
            self.defines.append(define.cover(sense))
        return self.__dict__


    def cover_none(self, dict:Tag) -> None:
        self.pos = dict.select_one('span.pos.dpos').text   

    def cover_voice(self, dict:Tag) -> None:

        uk_source = dict.select_one("span.uk.dpron-i source[type='audio/mpeg']")
        us_source = dict.select_one("span.us.dpron-i source[type='audio/mpeg']")

        self.us_pron = dict.select_one("span.us.dpron-i span.pron.dpron").text
        self.uk_pron = dict.select_one("span.uk.dpron-i span.pron.dpron").text

        self.us_voice = urljoin(DOMAIN,us_source['src'])
        self.uk_voice = urljoin(DOMAIN,uk_source['src'])