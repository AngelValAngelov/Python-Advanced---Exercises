names = {name: {} for name in input().split(", ")}

while True:
    item_cost = input()
    if item_cost == "End":
        break
    item_cost = item_cost.split("-")

    name = item_cost[0]
    item = item_cost[1]
    prise = item_cost[2]

    if item not in names[name]:
        names[name][item] = int(prise)

[print(f"{name} -> Items: {len(names[name])}, Cost: {sum(names[name].values())}") for name in names]