#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(text):
    """Return the first five characters of the given string"""
    return text[:5]

def last_seven(text):
    """Return the last seven characters of the given string"""
    return text[-7:]

def middle_number(number):
    """Return the second and third characters of the given number as a string"""
    number_str = str(number)
    return number_str[1:3]

def first_three_last_three(text1, text2):
    """Return a string made of first 3 chars of text1 and last 3 chars of text2"""
    return text1[:3] + text2[-3:]


if __name__ == '__main__':
    print(first_five(str1))          # Hello
    print(first_five(str2))          # Senec
    print(last_seven(str1))          # World!!
    print(last_seven(str2))          # College
    print(middle_number(num1))       # 50
    print(middle_number(num2))       # .5
    print(first_three_last_three(str1, str2))  # Helege
    print(first_three_last_three(str2, str1))  # Send!!
