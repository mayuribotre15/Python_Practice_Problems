# Given three integer number by user

a, b, c = map(int, input().split(' '))  # given three no. in 1 line separated by space ' '
no_list = list()
for i in (a, b, c):
    no_list.append(i)
no_list.sort()
print(no_list[1]) # print second largest no