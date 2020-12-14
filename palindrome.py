''' Write a function called is_palindrome that takes a string argument and returns
True if it is a palindrome and False otherwise. Remember that you can use
the built-in function len to check the length of a string '''
a=str(input("Enter the word:"))
def is_palindrome(a):
    if len(a) == 0:
        return True
    else:
        if a[0] == a[-1]:
            return is_palindrome(a[1:-1])
        else:
            return False

if(is_palindrome(a)==True):
    print("The string is a palindrome!")
else:
    print("The string isn't a palindrome!")