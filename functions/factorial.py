def factorial(number):
    if type(number) != int:
        raise BaseException("Number not given")

    fact = 1
    for i in range(1, number + 1):
        fact *= i
    
    return fact
