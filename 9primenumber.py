num1=int(input())
if num1 == 1:
    print("not prime")
if num1>1:
    for i in range(2,num1):
        if num1 % i == 0:
            print("not prime")
            break
    else:
        print("prime")    
    