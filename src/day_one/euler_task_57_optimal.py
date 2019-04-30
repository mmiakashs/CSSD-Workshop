
cache_result={1:(1,2)}

total=0
for i in  range(2,1001):
    numerator, denominator = cache_result[i-1]
    numerator = 2*denominator+numerator

    cache_result[i] = (denominator,numerator)

    numerator, denominator = cache_result[i]

    numerator = denominator+numerator
    if(len(str(numerator))>len(str(denominator))):
        total+=1

print(total)