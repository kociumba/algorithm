value1 = input("please input a number")

value2 = input("please input a second number")

value3 = input("please input a third number")

if value1 + value2 > value3 :
    if value2 + value3 > value1 :
        if value1 + value3 > value2 :
            print("this is a triangle")
        else :
            print("this is not a triangle")
    else :
         print("this is not a triangle")
else :
     print("this is not a triangle")