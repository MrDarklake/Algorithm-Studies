def minion_game(string):
    alphabe = []
    sessiz = []
    Stuart_puan = 0
    Kevin_puan = 0
    vowels = "AEIOU"
    for i in range(128):
        if "A" <= chr(i) <= "Z":
            alphabe.append(chr(i))
    for i in alphabe:
        if i not in vowels:
            sessiz.append(i)
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin_puan = len(string) - i + Kevin_puan
        elif string[i] in sessiz:
            Stuart_puan = len(string) - i + Stuart_puan
    if Kevin_puan > Stuart_puan :
        print ("Kevin",Kevin_puan)
    elif Stuart_puan > Kevin_puan:
        print("Stuart" , Stuart_puan)
    else:
        print("Draw")
    return 

if __name__ == '__main__':
    s = input()
    minion_game(s)