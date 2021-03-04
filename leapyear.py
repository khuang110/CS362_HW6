# Method for checking if given year is leap year
def leap_year(n):
    if n % 4 == 0:
        if n % 100 == 0:
            print(n, "is not a leap year")
        else:
            print(n, "is a leap year")
