attributes = list()

f = open("vhod.txt")

for line in f.readlines():
    value = line.strip()

    if value[0] == '+':
        attributes.append(value[1:])
    elif value[0] == '-':
        attributes.pop()
    else:
        count = 0
        for attribute in attributes:
            count += 1
            print(attribute, end="")
            if count < len(attributes):
                print('.', end="")

        print(" ", end="")
        print(value)

