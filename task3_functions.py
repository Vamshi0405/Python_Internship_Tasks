# Function to calculate factorial
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

# Random password generator
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print("Generated Password:", generate_password(12))

# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

string_input = input("Enter a string: ")
print("Palindrome:", is_palindrome(string_input))