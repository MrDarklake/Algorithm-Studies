def artan_alt_dizileri_bul(input_list):
    if not input_list or len(input_list) < 2:
        return []

    sonuc = []
    
    gecici_dizi = [input_list[0]]

    for i in range(1, len(input_list)):
        current_num = input_list[i]
        previous_num = input_list[i - 1]

        if current_num > previous_num:
            gecici_dizi.append(current_num)
        
        else:
            if len(gecici_dizi) >= 2:
                sonuc.append(gecici_dizi)
            
            gecici_dizi = [current_num]

    if len(gecici_dizi) >= 2:
        sonuc.append(gecici_dizi)
        
    return sonuc


input_1 = [1, 3, 2, 4, 6, 5, 8, 8]
output_1 = artan_alt_dizileri_bul(input_1)
print(f"Input 1: {input_1}")
print(f"Output 1: {output_1}") 

input_2 = [9, 7, 5, 6, 8]
output_2 = artan_alt_dizileri_bul(input_2)
print(f"Input 2: {input_2}")
print(f"Output 2: {output_2}")


"""
liste giriliyor
listenin icindeki degerleri artan bir grup gordu mu baska bir liste olustur

def artan_listeler(liste):
    return


if __name__ == "__main__":
    artan_listeler([1, 3, 2, 4, 6, 5, 8, 8])  # [1, 3, 2, 4, 6, 5, 8, 8] ----> [[1,3],[2,4,6],[5,8]]  olmasi gerek
    """
