print("List maker pro")
a=input("Enter item 1 name\n").strip().lower()
b=input("Enter item 2 name\n").strip().lower()
c=input("Enter item 3 name\n").strip().lower()
d=input("Enter item 4 name\n").strip().lower()
print("List checker pro")
e=input("Enter item name\n").strip().lower()
x=[a,b,c,d]
if e in x:
   print("yes",e,"is on the list")
else:
    print("no",e,"is not on the list")
