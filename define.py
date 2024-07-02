from bs4 import Tag,NavigableString

class Define:

    def __init__(self, tag: Tag):
        self.tag = tag
        self.leval = None
        self.define = None
    
    def cover_defines(self):

        deff = self.tag.select_one('div.def.ddef_d.db')
        print(deff.text)
        

    def cover_examples(self):

        list = self.tag.select('span.eg.deg')
        for i in list:
            print(i.text)


    def cover_leval(self) -> None:
        
        leval = self.tag.select_one("span.epp-xref.dxref")

        if leval:
            self.leval = leval.text

    def cover(self) -> None:

        self.cover_leval()
        self.cover_defines()
        self.cover_examples()