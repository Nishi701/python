#for i in range(10, 30, 1):
#    print(3*i)

multiples = [num for num in range(10, 31) if num % 3 == 0]
total_sum = sum(multiples)
print(total_sum)
