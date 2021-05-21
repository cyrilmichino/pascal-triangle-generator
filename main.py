cache = dict()
def pascaltriangle(n):
    
    if n in cache:
        return cache[n]

    elif n < 0:
        raise Exception("Sorry, no numbers below zero")

    elif n == 0:
        print("Any number to power zero is 1. Therefore, no pascal triangle")
        return None

    elif n == 1:
        return [1,1]
    
    else:
        pascal = [1]
        lst = pascaltriangle(n-1)

        for i in range(1, n):
            pascal.append(lst[i]+lst[i-1])
        
        pascal.append(1)
        cache[n] = pascal
        return pascal


for i in range(100):
    print(pascaltriangle(i))