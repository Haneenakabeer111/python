l1 = []
l2 = []
n = int(input("Enter the number of elements for list l1: "))
for i in range(n):
    u = int(input("Enter a value for l1: "))
    l1.append(u)
print("l1:", l1)
m = int(input("Enter the number of elements for list l2: "))
for i in range(m):
    v = int(input("Enter a value for l2: "))
    l2.append(v)
print("l2:", l2)
if len(l1) == len(l2):
    print("Lengths are the same.")
else:
    print("Lengths are not the same.")
if sum(l1) == sum(l2):
    print("Sum of l1 is equal to sum of l2.")
flag = 0
for x in l2:
    if x in l1:
        flag = 1
if flag == 1:
    print("There is a common element.")
else:
    print("There is no common element.")
