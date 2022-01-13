# t is no. of element in list
t = int(input())
list_no = []         #list_no = list()
for i in range(t):
    num = int(input())
    list_no.append(num)
list_no.sort()
for i in list_no:
    print(i)