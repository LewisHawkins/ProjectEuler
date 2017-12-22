n_natural_numbers = 100
sum_of_square = 0
square_of_sum = 0
for i in range(1, 1+n_natural_numbers):
    sum_of_square += i**2
for i in range(1, 1+n_natural_numbers):
    square_of_sum += i
square_of_sum **= 2
print(sum_of_square-square_of_sum)