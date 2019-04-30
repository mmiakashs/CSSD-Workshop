import math

#Check whether a given number is prime
def is_prime(num):
    if(num==2 or num==3):
        return True
    sq = int(math.sqrt(num))
    for i in range(2,sq):
        if(num%i==0):
            return False

    return True

#Finding the largest prime factor
num = 600851475143
sum = 0
fact = int(math.sqrt(num));
while(num>1):
    if(is_prime(fact) and num%fact==0):
        break
    fact-=1

print("Largest prime factor of {} is {}".format(num,fact))
