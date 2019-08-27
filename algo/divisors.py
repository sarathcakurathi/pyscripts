import math

def get_divisors(n):
    l = []
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            if n // i == i:
                l.append(i)
            else:
                l.append(i)
                l.append(n//i)
        i = i+1
    l.sort()
    return l

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    l = get_divisors(n)
    print(l)
