"""
Only x hours are left for the March Long Challenge and Chef is only left with the last problem unsolved.
However, he is sure that he cannot solve the problem in the remaining time. From experience,
he figures out that he needs exactly H hours to solve the problem.

Now Chef finally decides to use his special power which he has gained through years of intense yoga.
He can travel back in time when he concentrates. Specifically, his power allows him to travel to
N different time zones, which are T1,T2,…,TN hours respectively behind his current time.

Find out whether Chef can use one of the available time zones to solve the problem and submit it before
the contest ends.

Input
The first line of the input contains three space-separated integers N, H and x.
The second line contains N space-separated integers T1,T2,…,TN.
Output
Print a single line containing the string "YES" if Chef can solve the problem on time or "NO" if he cannot.
"""

# N is No. of time zone, H is Max time required to solve the problem, x is time left to solve the problem

N, H, x = map(int, input().split(' '))
T = list()
res = 'NO'
T.extend(map(int, (input().split(' '))))
if N == len(T):
    for i in T:
        i += x
        if i >= H:
            res = 'YES'
            break
    print(res)
else:
    print(f'Enter {N} no. of time zone')