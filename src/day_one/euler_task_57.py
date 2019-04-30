import sys
sys.setrecursionlimit(1010)

def expand_sq(iteration,expansion_num):
    if(iteration==expansion_num):
        return (1,2);
    numerator, denominator = expand_sq(iteration+1, expansion_num)
    numerator = 2*denominator+numerator
    return (denominator,numerator)

total=0
for i in  range(1,1001):
    numerator, denominator = expand_sq(1,i)
    numerator = denominator+numerator
    if(len(str(numerator))>len(str(denominator))):
        total+=1

print(total)