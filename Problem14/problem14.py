import time
import operator
start = time.time()
def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return (3*n) + 1
def keywithmaxval(d):
    """ a) create a list of the dict's keys and values; 
        b) return the key with the max value"""  
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]
longest_chain = [0,0]
dictionary = {}
for i in range(2,1000001):
    number = i
    incomplete = True
    chain = 0
    while incomplete:
        if number in dictionary.keys():
            incomplete = False
            chain += dictionary[number]
        else:
            number = int(collatz(number))
            chain += 1
        if number == 1:
            incomplete = False
    dictionary[i] = chain
print(keywithmaxval(dictionary))
print(time.time()-start)