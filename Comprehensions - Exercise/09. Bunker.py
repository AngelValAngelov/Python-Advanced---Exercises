materials = {x : {} for  x in input().split(", ")}

n = int(input())

for _ in range(n):
    info = input().split(" - ")
    material = info[0]
    kind_material = info[1]
    quality_quantity = info[2]

    qual_quan = [x for x in quality_quantity.split(";")]
    quantity = [x for x in qual_quan[0].split(":")][1]
    quality = [x for x in qual_quan[1].split(":")][1]

    materials[material][kind_material] = [quantity, quality]

r = [[[int(y) for y in materials[material][x]] for x in materials[material]] for material in materials]
result = sum([sum([y[0] for y in x]) for x in r])

print(f"Count of items: {result}")
print(f"Average quality: {sum([sum([y[1] for y in x]) for x in r])/ len(materials):.2f}")
[print(f"{y} -> {', '.join([x for x in materials[y]])}") for y in materials]
