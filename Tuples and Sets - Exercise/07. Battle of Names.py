number = int(input())

set_even = set()
set_odd = set()

for i in range(1, number + 1):
    name = input()
    summ = sum([ord(x) for x in name]) // i
    if summ % 2 == 0:
        set_even.add(summ)
    else:
        set_odd.add(summ)

odd_sum = sum(set_odd)
even_sum = sum(set_even)

if odd_sum == even_sum:
    print(', '.join([str(x) for x in set_odd.union(set_even)]))
elif odd_sum > even_sum:
    print(', '.join([str(x) for x in set_odd.difference(set_even)]))
else:
    print(', '.join([str(x) for x in set_odd.symmetric_difference(set_even)]))