def kartezyen(a,b):
    sonuc = []
    for i in a:
        for j in b:
            sonuc.append((i,j))
    for i in sonuc:
        print(i, end = " ")

if __name__ == "__main__":
    a = input()
    b = input()
    a1 = a.split()
    b2 = b.split()
    A = [int(x) for x in a1]
    B = [int(x) for x in b2]
    kartezyen(A,B)