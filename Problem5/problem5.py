number = 20
DIVISORS = [i for i in range(1,21)]
incomplete = True
while incomplete:
    true_table = ["T" for i in range(len(DIVISORS))]
    for i, div in enumerate(DIVISORS):
        if number % div == 0:
            true_table[i] = "F"
    if "T" not in true_table:
        incomplete = True
    print(number)
    number += 10
