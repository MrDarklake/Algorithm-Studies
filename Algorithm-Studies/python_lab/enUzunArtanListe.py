def EnUzunArtanListe(liste):
    en_uzun = 0
    en_uzun_liste = []
    long = len(liste)
    Artan_Listeler = []
    temp_list =[liste[0]]
    for i in range(1,long):
        if liste[i] > liste[i-1]:
            temp_list.append(liste[i])
        else:
            if len(temp_list) > 1:
                Artan_Listeler.append(temp_list.copy())
            temp_list = [liste[i]]
    Artan_Listeler.append(temp_list.copy())
    en_uzun = len(Artan_Listeler[0])
    for i in Artan_Listeler:
        if en_uzun < len(i):
            en_uzun = len(i)
            en_uzun_liste.append(i)
    for i in Artan_Listeler:
        if (i not in en_uzun_liste)  and  (len(i) == en_uzun) :
            en_uzun_liste.append(i)
        
    
    return en_uzun_liste

print(EnUzunArtanListe([1,4,3,4,5,3,7,8]))
