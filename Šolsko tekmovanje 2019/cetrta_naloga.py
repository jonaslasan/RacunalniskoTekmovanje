# n je stevilo, r in l sta listi (array)
def najvecja_vrednost_dobrote(n, r, l):
    dobrota = list()

    for i in range(n):
        stRozin = r[i]
        stLesnikov = l[i]
        delta = stLesnikov - stRozin

        dobrota.append(delta)
        naj_odsek = None

    for i in range(n):
        dolzina_skupine = i + 1
        potrebne_iteracije = n - dolzina_skupine + 1

        for j in range(potrebne_iteracije):
            skupina = dobrota[j:dolzina_skupine + j]  # Vrne odrezan sub-list
            sestevek = sum(skupina)  # vrne sestevek array-a

            # Lokalni maksimum
            if naj_odsek is None:
                naj_odsek = sestevek
            elif sestevek > naj_odsek:
                 naj_odsek = sestevek

    print(naj_odsek)

najvecja_vrednost_dobrote(4, [3, 1, 4, 0], [2, -5, 3, 4, -6])
