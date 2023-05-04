

with open("pcparts.txt","r", encoding="utf-8") as resz:
    alkatresz = [p.strip().split("#") for p in resz]
    # for sor in alkatresz:
    #     oszlop = sor.strip().split("#")
    #     print(oszlop[0])

def a_resz():
    print(f"A alkatrészek száma: {len(alkatresz)} db")
a_resz()