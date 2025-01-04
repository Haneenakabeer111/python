l1=[]
n=int(input("enter a limit:"))
for i in range(n):
    v=int(input("enter the values:"))
    l1.append(v)
print(l1)
c=[x for x in l1 if x%2!=0]
print("list of non even numbers:",c)
