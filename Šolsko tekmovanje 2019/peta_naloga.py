isGolombovo = True
isPopolno = True

mozni_intervali = []
stevio_oznak = None
oznake = []  # nov list (array)

# Vhodni podatki
with open("peta_besedilo.txt", "r") as f:
    for line in f:
        if stevio_oznak is None:
            stevio_oznak = int(line)
        else:
            oznake.append(int(line))
            mozni_intervali = [None] * int(line)

vsi_celostevilski_intervali = list(range(1, oznake[-1] + 1))

for i in range(stevio_oznak - 1):
    for j in range(i + 1, stevio_oznak):
        interval = oznake[j] - oznake[i]

        if isGolombovo:
            if mozni_intervali[interval - 1] == None:
                mozni_intervali[interval - 1] == 1
            else:
                isGolombovo = False

        vsi_celostevilski_intervali.remove(interval)

if len(vsi_celostevilski_intervali) > 0:
    isPopolno = False

print("je golombovo: " + str(isGolombovo))
print("je popolno: " + str(isPopolno))
