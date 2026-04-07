list = [1,2,4,5,6,13,35]

# Q1--------printing sum ,avg.max and min--------------
avg = sum(list)/len(list)
print(f"Average: {avg}")
print(f"Sum: {sum(list)}")
print(f"Maximum: {max(list)}")
print(f"Mininum: {min(list)}")

# Q2--------------Count Even and Odd--------------------
ecount = 0
ocount = 0
for i in list:
    if i % 2==0:
        ecount +=1
        
    else:
        ocount+=1
        
print(f"Even count: {ecount}")
print(f"Odd count: {ocount}")

# Q3---------Remove Duplicate from list---------------
lst = [1,2,2,3,4,4,5]
sin_lst = []

print(f"original List: {lst}")
for i in lst:
    if i not in sin_lst:
        sin_lst.append(i)
lst=sin_lst
       
print(f"list without duplicate: {lst}")

# Q4---------reverse a string using slicing--------------

str = "nihao"
rev = str[::-1]
print(rev)

# Q5---------print even number from 1 to 20 -----------

for i in range(1,21):
    if i % 2==0:
        print(i)

# Q6---------multiply list of element by 2--------------
ele = [5,10,15,20,6,11,2,13]
new_lst = [i * 2 for i in ele]
print(new_lst)
        
# Q7----------Count number greater than 9------------
count = len([i for i in ele if i>9])
print(count)





