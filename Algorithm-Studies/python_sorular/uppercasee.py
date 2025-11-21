def uppercasee(word):
    my_list = word.split(" ")
    sonuc = []
    for i in my_list:
        sonuc.append(i.capitalize())
    return " ".join(sonuc)


print(uppercasee("mike   SELAM"))





"""

def solve(s):
    kelimeler = s.split(' ')
    capitalized_kelimeler = [kelime.capitalize() for kelime in kelimeler]
    return ' '.join(capitalized_kelimeler)

if __name__ == '__main__':
    frtp = open(os.environ['OUTPUT_PATH']. 'w')
    s = input()
    result = solve(s)
    frtp.write(result + '\n')
    frtp.close()

# burayi for dongusunu nasil listeye esitleyecegimizi gostermek icin yazdim

"""