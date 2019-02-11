samoglasniki = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}

stevilo_samoglasnikov = 0
stevilo_angleskih_crk = 0

f = open("prva_besedilo.txt", "r")
a = True
for crka in f.read():
    if crka in samoglasniki:
        stevilo_samoglasnikov += 1

    vrednost_crke = ord(crka)

    if (ord('a') < vrednost_crke < ord('z')) or (ord('A') < vrednost_crke < ord('Z')):
        stevilo_angleskih_crk += 1


print("Stevilo samoglasnikov: " + str(stevilo_samoglasnikov))
print("Stevilo angleskih crk: " + str(stevilo_angleskih_crk))