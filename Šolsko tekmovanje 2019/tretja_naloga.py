f = open("tretja_vhod.txt", "r")

prva_vrstica = f.readline()
druga_vrstica = f.readline()

# V primeru kaže vhodni podatek kot "n x y"
prvi_podatki = prva_vrstica.split()  # To vrne ['n', 'x', 'y']

# Parse to int
n = int(prvi_podatki[0])
x = int(prvi_podatki[1])
y = int(prvi_podatki[2])

rotacija_robota = 0

for ukaz in druga_vrstica:
    if ukaz == 'N':
        if rotacija_robota % 4 == 0:
            x += 1
        if rotacija_robota % 4 == 1:
            y -= 1
        if rotacija_robota % 4 == 2:
            x -= 1
        if rotacija_robota % 4 == 3:
            y += 1

    if ukaz == 'L':
        rotacija_robota -= 1

    if ukaz == 'D':
        rotacija_robota += 1

print("x: " + str(x) + "; y: " + str(y))
