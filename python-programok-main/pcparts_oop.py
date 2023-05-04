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

print("###############################################")

print(f"Az alkatrészek száma: {len(pc_parts)} db")

print("###############################################")

osszeg = 0
for item in pc_parts:
    osszeg = osszeg + item.ar
print(f"Az alkatrészek összárai: {osszeg} Ft")

legdragabb = max(pc.ar for pc in pc_parts)
for item in pc_parts:
    if item.ar == legdragabb:
        print(f"A legdrágább alkatrész: {item.nev}")

legolcsobb = min(pc.ar for pc in pc_parts)
for item in pc_parts:
    if item.ar == legolcsobb:
        print(f"A legolcsóbb alkatrész: {item.nev}")  

kompa = (pc.ar for pc in pc_parts)
for item in pc_parts:
    if item.kompatibilis == ("kompatibilis"):
        print(f"Az alkatrész: {item.nev} kompatibilis")  