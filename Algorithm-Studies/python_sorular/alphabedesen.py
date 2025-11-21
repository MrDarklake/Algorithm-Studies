def print_rangoli(size):
    satir_boy = size*4 -3
    alphabe = []
    my_list = []
    all_satirlar = []
    #import string                          bu soldaki iki satırlık kod aşağıda alfabeyi oluşturmak için kullandığım 7 satırla aynı işlevde
    #alphabet = string.ascii_lowercase      
    for i in range(128):
        k = chr(i)
        if "a" <= k <= "z":
            alphabe.append(k)
        else:
            pass
    for i in alphabe[:size]:
        my_list.append(i)
    my_list = list(my_list[::-1])

    for i in range(size):
        sol_taraf = my_list[:i+1]
        sag_taraf = sol_taraf[::-1][1:]
        all_satir = sol_taraf + sag_taraf
        tamamlanmis_satir = "-".join( all_satir )
        tamamlanmis_satir_v2 = tamamlanmis_satir.center(satir_boy,"-")
        all_satirlar.append(tamamlanmis_satir_v2)
    alt_satirlar = all_satirlar[::-1][1:]
    all_satirlar.extend(alt_satirlar)
    print("\n".join(all_satirlar))
    return 

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    