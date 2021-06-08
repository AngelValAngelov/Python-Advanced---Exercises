country = input().split(", ")
capital = input().split(", ")

result = {x[0]: x[1] for x in zip(country, capital)}
[print(f"{key} -> {value}") for key, value in result.items()]