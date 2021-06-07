words = input().split(", ")

result = {x:len(x) for x in words}
solved = [f"{x} -> {y}" for x,y in result.items()]
print(', '.join(solved))



