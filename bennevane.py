# szoveg = "ezegyszöveg"
# if "v" in szoveg:
#     print("benne van")
# else:
#     print("nincs")

# szoveg = "ezegyszöveg"
# beker = input("Kérem a betűt")
# if beker in szoveg:
#     print(f"{beker}betű benne van a szövegben")
# else:
#     print(f"{beker}betű nincs benne a szövegben")

# szoveg = "KEDD"
# print(szoveg.lower())


# hetnapjai = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]

# beker = input("Kérem a napot! ").lower()

# if beker in hetnapjai:
#     print(f"{beker}nap benne van a listában")
# else:
#     print(f"{beker}nap nincs benne a listában")







garazs = ["toyota", "bmw", "subaru", "mitsubishi", "peugeot", "ford"]

# for i in range(len(garazs)):
#     garazs[i] = garazs[i].lower()

#elemek konvertálása kisbetűvé:
garazs_kisbetu = [item.lower()for item in garazs]

 #elemek konvertálása nagybetűvé:
garazs_nagybetu = [item.upper()for item in garazs]

# marka = input("Kérek egy autómárkát! ").upper()

# if marka in garazs_nagybetu:
#     print(f"{marka} megvan")
# else:
#     print(f"{marka} még nincs meg")

print(garazs[0][-1])
