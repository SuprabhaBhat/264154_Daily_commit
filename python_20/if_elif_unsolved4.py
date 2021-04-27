# Write a python program to check if the input number is-real number-float numner-string-complex number-Zero (0)

a=input()
if(type(a)==float):
    print('this is floating number')

elif(type(a)==int):
    print('this is integer number')


elif (type(a) == str):
    print('this is string')

elif(type(a)==complex):
    print('this is complex number')

else:
    print('you entered zero')

