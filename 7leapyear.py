year=int(input())
if (year % 400==0 ) and (year % 100 == 0):
    print("leap year")
elif (year % 100!=0) and ( year % 4 == 0):
    print("leap yearr")
else:
    print("not")        