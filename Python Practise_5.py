'''
Author: Adityaraj Yadav 
Date: 8 January 2022
Project Name: Palindrome less 10 Test
Purpose:For Practising Purpose
'''


def comming_palindrome(n):
    # this will return the number directly if it is less than 10 and exit the program
    if n < 10:
        return n
        exit()
    n += 1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    # this is cheking whether the number is palindrome or not
    return str(n) == str(n)[::-1]

Times = int(input("Enter how many numbers you want to show there Palindrome: "))
list = []

for i in range(Times):
    # Taking input and appending to the empty list 
    list_num = int(input("Enter the numbers: "))
    list.append(list_num)
for i in range(Times):
    # printing the number if it is greater than 10
    if n>10:
        print(
            f"The next palindrome for the number {list[i]} is {comming_palindrome(list[i])}")
    # printing the number if it is less than 10
    else:
        print("You have entered a number which is less than 10")