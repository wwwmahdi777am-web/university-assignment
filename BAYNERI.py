def decimal_to_binary(decimal_num): if decimal_num == 0: return "0"
remainders = []
n = decimal_num

while n > 0:
    remainder = n % 2
    quotient = n // 2
    
    remainders.append(str(remainder))
    n = quotient
    
remainders.reverse()
binary_result = "".join(remainders)

return binary_result
user_input = int(input()) final_binary = decimal_to_binary(user_input) print(final_binary)