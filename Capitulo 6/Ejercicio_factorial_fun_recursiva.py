

def factorial(num): 
    if num > 0:
         n = num * factorial(num-1)
         print(n)
    else:
        n = 1
    return n
    
factorial(15)
