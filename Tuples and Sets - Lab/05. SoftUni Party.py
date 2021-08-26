number_ofguests = int(input())

guests = set()
available = set()

for i in range(number_ofguests):
    guest = input()
    guests.add(guest)

while True:
    guest = input()
    if guest == "END":
        break
    else:
        available.add(guest)

unavailable = guests - available

print(len(unavailable))
print("\n".join(sorted(unavailable)))





