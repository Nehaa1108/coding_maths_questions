lower=int(input())
upper=int(input())

for i in range(lower,upper+1):
    if i>1:
        for n in range(2,i):
            if i % n ==0:
              
                break
        else:
            print("prime",i)        
