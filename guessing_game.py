print("yo yaal welcome to the number guessing gameee!")
print("let's get started, woooo!!")
import random
num=random.randint(1,10)
a=0
while a<5:
    a+=1
    i=int(input("enter a number:"))
    if num<i:
        print("the number is lower than that!!, keep guessing")
    if num>i:
        print("the number is higher than than that, keep guessing")
    if num==i:
        print("WHOOPIE,YOU GUESSED IT IN" , a , "ATTEMPTS!!")
        break
        print("the number was",num)