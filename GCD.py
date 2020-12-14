''' TO FIND GCD(GREATEST COMMON DIVISOR)OF GIVEN TWO NUMBER'''
a= int(input("Enter number1: "))
b= int(input("Enter number2: "))
def get_gcd(a, b):
    while b:
        a, b = b, a%b
    return a
print(get_gcd(a, b))