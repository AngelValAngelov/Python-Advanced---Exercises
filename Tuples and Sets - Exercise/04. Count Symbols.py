text = input()

signs = {}

for sign in text:
    if sign not in signs:
        signs[sign] = 0
    signs[sign] += 1

for sign, quantity in sorted(signs.items()):
    print(f"{sign}: {quantity} time/s")
