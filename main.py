from dictionary import Dictionary

di = Dictionary("key")
di.process()

with open("target.json", "w") as f:
    f.write(di.__str__())