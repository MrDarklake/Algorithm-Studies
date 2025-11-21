def index_sozluk (liste):
    index_sozlugu = {}
    index_sirasi = 0
    for i in liste:
        for j in range(len(i)):
            if j not in index_sozlugu:
                index_sozlugu[j] = [i[j]]
            else:
                index_sozlugu[j].append(i[j])
    return index_sozlugu

x = index_sozluk(["cat","dog","bat"])
print(x)
