# Fizzbuzz return number between 1 - 100
# print fizz if mult of 3 and fizzbuzz if mult of 5 and 3
def fizz_buzz(n):
    if n < 1 or n > 100:
        return None
    elif n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)


