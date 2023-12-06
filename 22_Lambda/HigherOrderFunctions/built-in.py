from functools import reduce

numbers = [3, 6, 8, 12, 23]

squared_nums = map(lambda num: num * num, numbers)

# print(squared_nums)       #    <map object at 0x7f5193d5fa00>

print(list(squared_nums))
#   [9, 36, 64, 144, 529]


odd_nums = filter(lambda num: num % 2 != 0, numbers)

# print(odd_nums)           #   <filter object at 0x7fb74255fac0>

print(list(odd_nums))
#   [3, 23]


numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)  # 15

# built-in function
print(sum(numbers))  # 15

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)  # 25

# built-in function
print(sum(numbers, 10))  # 25