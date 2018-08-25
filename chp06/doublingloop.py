def doubles(num):
    k=1
    while(k<4):  #to make sure it does doubling 3 times
        num=num*2
        print(num)
        k=k+1


user_input=float(input("Enter the digit ="))
user_input=doubles(user_input)
