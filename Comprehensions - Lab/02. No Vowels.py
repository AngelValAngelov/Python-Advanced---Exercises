text = input()

result = [x for x in text if x not in ["a","o","u","e","i","A","O","U","E","I"]]

print("".join(result))