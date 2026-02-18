def classify_number(n: int):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def first_n_primes(n: int):
    primes = []
    num = 2
    while len(primes) < 10:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
            print(num)
        num += 1
    return primes

def sum_1_to_100():
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total

def main():

    print(classify_number(6))
    print(classify_number(-9))
    print(classify_number(0))
    first_n_primes()
    print(sum_1_to_100())
