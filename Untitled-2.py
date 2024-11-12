def getprime(n):
    result = [1,]
    for i in range(2,n):
        count_del = 0
        for j in range(2 , i -1):
            if i % j == 0:
                count_del += 1
        if count_del == 0:
            result.append(i)
    return result
print(getprime(10))