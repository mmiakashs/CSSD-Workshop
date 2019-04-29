cache_result={}

def cal_chain_length(n):
    if(n==1):
        return 1
    elif(n in cache_result):
        return cache_result[n]

    if n%2==0:
        cache_result[n] = cal_chain_length(n//2)+1
    else:
        cache_result[n] = cal_chain_length(3*n+1) + 1
    return cache_result[n]

num=int(1e6)
max_chain_length=1
max_chain_number = 1
for i in range(1,num):
    chain_length = cal_chain_length(i)
    if(chain_length>max_chain_length):
        max_chain_length = chain_length
        max_chain_number = i

print("Maximum chain length is generated when the number is {} and the chain length is {}"
      .format(max_chain_number,max_chain_length))
