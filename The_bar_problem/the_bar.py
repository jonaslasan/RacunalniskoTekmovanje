"""
For a given metal bar of length n and given prices per meters,
What is the most money you can make by splitting and selling the bar?

Example prices:
1 meter = 1 €
2 meter = 5 €
3 meter = 8 €
4 meter = 12 €
5 meter = 16 €
6 meter = 17 €
7 meter = 20 €
"""

price = [1, 5, 8, 12, 16, 17, 20]

memoize = dict()


def cut(bar_length, level):

    if bar_length <= 0:
        return 0

    if bar_length in memoize:
        return memoize[bar_length]

    local_max = 0
    for left_cut in range(len(price)):
        if bar_length - left_cut <= 0:
            break

        left_value = price[left_cut]

        right_value = cut(bar_length - (left_cut + 1), level + 1)

        if right_value + left_value > local_max:
            local_max = right_value + left_value

    print(" " * level, "Length: ", bar_length, " --> Optimal price: ", local_max)
    memoize[bar_length] = local_max
    return local_max


result = cut(18, 0)
print("Best price: ", result)
