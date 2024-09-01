s = input()
w = int(s.split(' ')[0])
h = int(s.split(' ')[1])
x = int(s.split(' ')[2])
y = int(s.split(' ')[3])
r = int(s.split(' ')[4])
if r <= x <= w - r and r <= y <= h - r:
    print("Yes")
else:
    print("No")
