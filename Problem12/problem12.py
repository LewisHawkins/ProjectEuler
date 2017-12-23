import math
incomplete = True
i = 1
total = 0
while incomplete:
    divisor_list = []
    total += i
    i += 1
    max_divisor = math.ceil(math.sqrt(total))
    for divisor in range(1,max_divisor):
        if total / divisor == total // divisor:
            divisor_list.append(divisor)
            divisor_list.append(total/divisor)
    if len(divisor_list) > 500:
        print(str(total) + ": " + str(divisor_list) + ": " + str(len(divisor_list)))
        incomplete = False
