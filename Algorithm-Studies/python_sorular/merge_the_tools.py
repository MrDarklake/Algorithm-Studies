def merge_the_tools(string, k):

    temp_string = ""
    index_sayisi = 0
    liste_sayisi = int(len(string) / k)
    yeni_listeler = []
    temp_list = []
    sonuc_listler = []

    for i in range(liste_sayisi):                    
        for j in range(k):
            temp_list.append(string[index_sayisi])   
            index_sayisi += 1 
        yeni_listeler.append(temp_list)
        temp_list = []

    for i in range(liste_sayisi):
        for j in yeni_listeler[i]:
            if j not in temp_list:
                temp_list.append(j)
        sonuc_listler.append(temp_list)
        temp_list = []

    for i in range(liste_sayisi):
        for j in sonuc_listler[i]:
            temp_string += j
        print(temp_string)
        temp_string = ""
        

if __name__ == '__main__':
    string , k = input() , int(input())
    merge_the_tools(string , k)



"""                                                      ****yapay zekanin cozumu****

def merge_the_tools_pythonic(string,k):
    n = len(string)

    # 1. adim : k adimli range ile parcalari direkt al
    # i , her parcanin baslangic indeksidir (0,3,6...)
    for i in range(0, n, k):
        # 2. adim : parcayi al (exp : "AAB")
        t = string[ i : i + k]

        # 3. adim : tekrarlari temizle (u 'yu olustur)
        u = ""
        seen_chars = set() # O(1) hizinda kontrol icin set kullan

        for cahr in t:
            # eger bu karakteri set'te daha once gormediysek
            if char not in seen_char:
                u += char # sonuc stringine ekle (sirayi koru)
                seen_chars.add(char) # set'e ekle ki bir daha geldiginde atlayalim
        
        # 4. adim yazdir
        print(u)
        










"""