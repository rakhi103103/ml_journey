# Q8------largest number-------------
lst=[3,12,7,15,9]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print(f"List: {lst}")
print(f"Largest number: {largest}")

# Q9---------Swap two number-------------
a=8
b=10
temp = 0
print(f"a={a} b={b}")
temp=a
a=b
b=temp
print(f"a={a} b={b}")

# Q10--------print square from 1 to 5--------
for i in range(1,6):
    i*=i
    print(i)

# Q11---------Print Numbers from 1 to 50 with Step 5------
for i in range(1,51,5):
    print(f"\n {i}")

# Q12----------ount number divisible by 3----------------
arr = [3,5,9,10,15,22,18]
count = len([i for i in arr if i %3==0])
print(f"Count number divisible by 3 is {count}")

# Q13--------Sum of Odd Numbers from 1 to 20----------------
sum = 0
for i in range(1,20):
    if i%2 !=0:
        sum+=i
print(sum)

# Q14----------largest number in list---------------------
listt = [22,35,1,78,5,7,68]
max_num = listt[0]
for i in listt:
    if i > max_num:
        max_num = i
print(f"the largest number is {max_num}")

# Q15-------------Reverse a List-------------------
ls = [22,35,1,78,5,7,68]
reve = ls[::-1]
print(reve)

# Q16---------Check Palindrome Number----------------

num= int(input("Enter 3 didgit number to check palidrone number: "))
ori = num
res = 0
while num>0:
    rem = num % 10
    res= (res*10) + rem
    num = num//10
if ori == res:
    print(f"since {ori} and {res} are same ,it is palidrone")
else:
    print(f"since {ori} and {res} are not same ,it is not palidrone")

# Q17------------Find Duplicate Elements in List----------------

lsst = [1,2,2,3,4,4]
dup = []
for i in lsst:
    if lsst.count(i)>1 and i not in dup:
        dup.append(i)
for i in dup:
    print(i)


    




