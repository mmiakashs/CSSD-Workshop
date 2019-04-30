#storing all the fibonacci numbers
fib = {1: 1, 2: 2}

#Calculating the nth fibonacci number
def fibonacci(n):

    if (n in fib):
        return fib[n]

    # Calculating and storing the nth fibonacci numbers for later use
    fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib[n]

#Calculating the summ of all even fibonacci numbers
i = 1
sum = 0
num = 4000000
while (True):
    res = fibonacci(i)
    if (res > num):
        break
    if (res % 2 == 0):
        sum += res
    i+=1

print("Sum of all the fibonacci numbers from 1 to {} is {}".format(num,sum))