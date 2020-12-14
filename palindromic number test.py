''' TO CHECK IF THE GIVEN NUMBER IS A PALINDROME '''
num = input('Enter a number : ')

if num == str(num)[::-1]:
      print('The given number is palindrome')
else:
      print('The given number is not a palindrome')