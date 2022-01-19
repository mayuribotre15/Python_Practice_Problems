"""
Find the Direction:
Chef is currently facing the north direction. Each second he rotates exactly 90 degrees in clockwise direction.
Find the direction in which Chef is facing after exactly X seconds.

Note: There are only 4 directions: North, East, South, West (in clockwise order).

Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single integer X.
Output Format
For each testcase, output the direction in which Chef is facing after exactly X seconds.
"""
# t is no. of test cases
t = int(input())
direction = ""
for i in range(t):
    # sec is seconds
    sec = int(input())
    if sec % 4 == 0:
        direction = 'North'
    elif sec % 4 == 1:
        direction = 'East'
    elif sec % 4 == 2:
        direction = 'South'
    elif sec % 4 == 3:
        direction = 'West'
    else:
        direction = 'Please enter valid integer no.'
    print(direction)
