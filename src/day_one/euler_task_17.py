unit_numbers = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
                5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
after_tens = {10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",
              14:"Fourteen",15:"Fifteen",16:"Sixteen", 17:"Seventeen",
              18:"Eighteen",19:"Nineteen"}
tens = {2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty", 7:"Seventy",8:"Eighty",9:"Ninety"}


def number_to_words(num):

    res = ""
    and_flag = False
    if(num>=1000):
        res += unit_numbers[num//1000] + "Thousand"
        if(num%1000==0):
            return res
        num %= 1000
        and_flag=True

    if(num>=100):
        res += unit_numbers[num//100] + "Hundred"
        if (num % 100 == 0):
            return res
        num %= 100
        and_flag = True

    if(num>=20):
        if (and_flag):
            res += "And"
            and_flag = False

        res += tens[num//10]
        if(num%10==0):
            return res

        num %= 10

    if (num in after_tens):
        if (and_flag):
            res += "And"
            and_flag = False
        res += after_tens[num]

    if (num in unit_numbers):
        if (and_flag):
            res += "And"
        res += unit_numbers[num]

    return res

total_len = 0
for i in range(1,1001):
    converted_number = number_to_words(i)
    # print(i,converted_number,len(converted_number))
    total_len += len(converted_number)

print(total_len)