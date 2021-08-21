phonebook = {}

while True:
    name_phone_number = input()
    if name_phone_number[0].isdigit():
        break
    name_phone_number = name_phone_number.split("-")
    name = name_phone_number[0]
    number = name_phone_number[1]
    phonebook[name] = number

searching_names = int(name_phone_number)

for i in range(searching_names):
    searching_name = input()
    if searching_name not in phonebook.keys():
        print(f"Contact {searching_name} does not exist.")
    else:
        print(f"{searching_name} -> {phonebook[searching_name]}")

