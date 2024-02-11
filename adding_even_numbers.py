input = int(input())
sum_even = 0

for number in range(1, input + 1):
    if number % 2 == 0:
        sum_even += number

print(sum_even)