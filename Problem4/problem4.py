#Used in the for loop to reduce loading time
LOWER_BOUND = 100 +1
UPPER_BOUND = 999 + 1
#more refined
def highest_pallindrome(low_bound, up_bound):
    pallindromes = []
    for i in range(low_bound, up_bound):
        for j in range(i, up_bound):
            number = i * j
            string = str(number)
            if string == string[::-1]:
                pallindromes.append(number)
    pallindromes.sort(reverse=True)
    print(pallindromes[0])
highest_pallindrome(LOWER_BOUND, UPPER_BOUND)
