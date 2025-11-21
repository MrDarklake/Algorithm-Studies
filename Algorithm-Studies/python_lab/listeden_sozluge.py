def listeden_sozluge (liste):
    harf_sozlugu = {}
    harf_sayisi = 0
    duzenlenmis_liste = []
    temp_list = []
    for i in liste:
        for j in range(10):
            if len(i) == j:
                temp_list.append(i)
        duzenlenmis_liste.append(temp_list)
        temp_list = []
    for i in duzenlenmis_liste:
        uzunluk = len(i[0])
        if uzunluk in harf_sozlugu:
            harf_sozlugu[uzunluk].append(i)
        else:
            harf_sozlugu[uzunluk] = i
    return harf_sozlugu

output = listeden_sozluge(["apple", "banana", "kiwi", "grape", "orange"])
print(output)