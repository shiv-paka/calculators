sum1=int(input("Enter the first number: "))   
sum2=int(input("Enter the second number: "))   
sqr= lambda num,num1:num**num1
print(sqr(sum1,sum2))

something=lambda n1:n1*n1*n1
print(something(4))

nSquare= lambda N1:N1*N1
nList=[1,2,3,4,5,6,7,8,9,10]
sList=[]
for ele in nList:
  sList.append(nSquare(ele))
print(sList)
print()
print("============================")
def square(Num1):
  lst=[]
  for ele in Num1:
    lst.append(ele*ele)
  print(lst)
lst12=[11,12,13,14,15,16,17,18,19,20]
print(square(lst12))
print()
print("============================")
def cube(Num2):
  return Num2*Num2*Num2
new_lst=list(map(cube,lst12))
print(new_lst)
print()
print("============================")
Cube_1=lambda lcube: lcube*lcube*lcube
new_list1=list(map(Cube_1,nList))
print(new_list1)

print()
print("============================")

new_list1=list(map(lambda lcube: lcube*lcube*lcube,nList))
print(new_list1)

print()
print("========================================================")
remNew=list(map(lambda num:num%3,lst12))
print(remNew)

lst=[1,2,3,4,5,6,7,8,9,0]
new_list=[]
new_list2=[]
for ele in lst:
  if ele%2==0:
    new_list.append(ele)
  
  else:
    new_list2.append(ele)
print(new_list)
print(new_list2)

check = lambda num:num%2==0
checkLst=[1,2,3,4,5,6,7,8,9,10]
new_lst3=list(filter(check,checkLst))
print(new_lst3)

