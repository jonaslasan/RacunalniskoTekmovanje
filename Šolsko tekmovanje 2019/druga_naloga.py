# Dolzine miz
d = [1, 2, 3, 4, 5, 6, 7]
stevilo_kroznikov = 0

for dolzina in d:
    veckratnik_tri = int(dolzina / 3)
    ostanek = dolzina % 3

    stevilo_kroznikov += veckratnik_tri * 5
    if ostanek == 1:
        stevilo_kroznikov += 1
    if ostanek == 2:
        stevilo_kroznikov += 3

print(stevilo_kroznikov)