pcpart = open("pcparts.txt","r",encoding="UTF-8")
print(pcpart.readline())
for sorok in pcpart:
    print(sorok.strip().split("#"))

with open("pcparts.txt","a", encoding="utf-8") as szamok:
    szamok.write(str(1))