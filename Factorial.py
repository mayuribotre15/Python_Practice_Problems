#calculate factorial
#Enter the no. of testcases
for i in range(int(input())):
    #Enter integer to calculate factorial
    num = int(input())
    fact = 1
    for j in range(1,num+1):
        fact *= j
    print(fact)