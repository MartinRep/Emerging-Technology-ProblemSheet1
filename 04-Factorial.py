def factorial(x):
    if x == 1: 
        result = x
        return result
    return x*factorial(x-1)

#Test
print factorial(10)