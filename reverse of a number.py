''' TO GET REVERSE OF A GIVEN NUMBER'''
number = int(input("Enter a number: "))
reverse = 0

while (number > 0):
    a = number % 10
    reverse = reverse * 10 + a
    number = number // 10

print(reverse)