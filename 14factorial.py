# num=int(input())
# fact=1
# if num<0:
#     print("not factorial")
# if num==0:
#     print(1)
# if num>0:        
#     for i in range(1,num+1):
#         fact=fact*i
# print(fact)    



# recursion

def fact(n):
    if n==0:
        return 1
    else:
        return ((n)*fact(n-1))
    
nu=int(input())
result=fact(nu) 
print(result)   