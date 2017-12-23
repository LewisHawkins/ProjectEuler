def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return (3*n) + 1
longest_chain = [0,0]
dictionary = {}
for i in range(1000000):
    chain = 0
print(longest_chain)
