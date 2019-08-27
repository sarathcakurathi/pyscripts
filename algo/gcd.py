from divisors import get_divisors

def getGCD(n1_divisors, n2_divisors):
    common = [val for val in n1_divisors if val in n2_divisors]
    return max(common)    

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

n1_divisors = get_divisors(n1)
n2_divisors = get_divisors(n2)

print("GCD of {}, {} is {}".format(n1, n2, getGCD(n1_divisors, n2_divisors)))