class pcparts:
      def  __init__(self, nev, kompatibilis,ar):
        self.nev = nev
        self.kompatibilis = kompatibilis
        self.ar = ar 
fajl = open("pcparts.txt","r",encoding="utf-8")

pc_parts = []
for sorok in fajl:
    oszlop = sorok.strip().split("#")
    pc_parts.append(pcparts(oszlop[0],oszlop[1],int(oszlop[2])))

for item in pc_parts:
    print(f"Név: {item.nev}, kompatibilis: {item.kompatibilis}, Ár: {item.ar}")

kompa = (pc.ar for pc in pc_parts)
for item in pc_parts:
    if item.kompatibilis == ("kompatibilis"):
        print(f"Az alkatrész: {item.nev} kompatibilis")