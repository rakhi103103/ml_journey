import numpy as np

# Q---------Q8 – Create Matrix -Create a 5×5 matrix like-------------------------

#creating 5x5 matix filled with 0
matrix = np.zeros((5,5),dtype=int)

#creating inner filed  with 1
matrix[1:4,1:4]=1

#center with 9
matrix[2,2]=9
print(matrix)

# Q ------------------Q9 – Replace Values---------------

arr = np.array([10,20,30,40,50])
arr[arr>30]=-1
print(arr)

# Q---------------Q10 – Normalize Array-------------------------------------
arr1 =np.array([10,20,30,40,50])
normalization = (arr1-arr1.min())/(arr1.max()-arr1.min())
print(f"The normalization of {arr1} is {normalization}")


# Q-----------Q11 – Find Unique Values with Count------------------------

arr2 = int(input("Enter the number of the array: "))
numm = []
for i in range(arr2):
    nu = int(input("Enter the name to check unique value: "))
    numm.append(nu)

arra = np.array(numm)
values,counts =np.unique(arra,return_counts=True)

for v,c in zip(values,counts):
    print(v,":",c)


# Q------------------Q12 – Row Mean----------------------------------
mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
row_mean = np.mean(mat,axis=1)
print(f"The mean for reavh row for the givn matrix {mat} is {row_mean}")

# Q----------------Q13 – Find Top 3 Largest Numbers-----------------------
ar = np.array([12,45,2,41,31,10])
top3 = np.partition(ar,-3)[-3:][::-1]
print(f"the top 3 max numbers in the given array {ar} is {top3}")

    



