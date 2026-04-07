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
    



