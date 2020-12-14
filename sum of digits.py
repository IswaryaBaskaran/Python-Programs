''' TO FIND THE SUM OF DIGITS OF A NUMBER'''
number = int(input("Enter a number: "))
def sumdigits(number):
  if number==0:
    return 0
  return (number%10) + sumdigits(number//10)

print(sumdigits(number))