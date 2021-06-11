rows, cols = [int(x) for x  in input().split(" ")]

matrix = [print(' '.join([f"{chr(97 + x)}{chr(97 + y + x)}{chr(97 + x)}" for y in range(cols)])) for x in range(rows)]



