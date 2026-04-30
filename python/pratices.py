# #Reverse a String without using slicing

# str ="hello"
# rev=""
# for char in str:
#     rev = char+rev
# print(rev)

# # as input frpm user

# str_input = input("Enter any word: ")
# rev_word = ""
# for char in str_input:
#     rev_word = char+rev_word
# print(rev_word)

# #count vowels and consonants in a string

# def count_vowel_consonants(string):
#     vowel = 0
#     consonant = 0

#     for i in string:
#         if i in 'aeiouAEIOU':
#             vowel+=1
#         elif i.isalpha():
#             consonant+=1
        
#     return vowel,consonant


# str = "nihao"
# v,c = count_vowel_consonants(str)
# print(f"vowel={v}")
# print(f"consonant={c}")

# #find the largest and smallest number in a list
# lst=list(map(int,(input("enter numbers in a list: ").split())))

# largest = lst[0]
# smallest = lst[0]
# for i in lst:
#     if i > largest:
#         largest =i
# for n in lst:
#     if n < smallest:
#         smallest = n

# print(f"List: {lst}")      
# print(f"largest number: {largest}")      
# print(f"smallest number : {smallest}")  

# #second method
# largest_num = max(lst)
# smallest_num = min(lst)
# print(f"largest number: {largest_num}")      
# print(f"smallest number : {smallest_num}") 

# #check if the number is palidrome
# def palidrome_num(num):
#     temp = num
#     rev = 0
#     while num >0:
#         rem = num % 10
#         rev = rev *10 +rem
#         num = num // 10
#     if rev ==temp:
#         print(f"since {rev} = {temp} it is palidrome")
#     else:
#         print(f"since {rev} is not {temp} it is not apalidrome")


# n= int(input("enter the number to check plaidrome number"))
# palidrome_num(n)

# #Print Fibonacci series up to n and calcute it.

# def fibonacci_s(n):
#     a,b=0,1
#     result=[]
#     total=0
#     for i in range(n):
#         result.append(a)
#         total+=a
#         a,b=b,a+b
#     return (result,total)
    
        

# fibo = int(input("enter the number to see the fibonacci series: "))
# print(f"The fibonacci series and it sum are {fibonacci_s(fibo)}")

# #count frequency of each number in a string
# word = input("enter the word: ")
# freq={}

# for char in word:
#     freq[char] = freq.get(char,0)+1
# print(freq)

# #alternate method
# for char in set(word):
#     print(char,": ", word.count(char))

# #remove duplicate from a list(without using set)
# letter = ["apple", "banana", "apple", "orange", "banana"]
# result=[]
# for char in letter:
#     if char not in result:
#         result.append(char)

# print(result)

# #check if a number is prime
# def is_prime(n):
#     if n <=1:
#         return False
    
#     for i in range(2,n):
#         if n % i==0:
#             return False
#     return True

# nums=int(input("Enter number to check prime or not: "))


# print(f"prime numbers: {is_prime(nums)}")

# #Find second largest number in a  list

# def sec_largest(num):
#     largest=num[0]
#     second=num[0]
    
#     for i in num:
#         if i>largest:
#             second=largest
#             largest=i
#         elif i>second and i!=largest:
#             second=i
#     return second

# second_lar = list(map(int,input("Enter numbers with spaces in between: ").split()))
# print("the numbers are: ",second_lar)
# print(f"The second largest number = {sec_largest(second_lar)}")

#merge two list and sort them without using sort
lst1=list(map(int,input("Enter numbers in LIST 1 with spaces in between: ").split()))
lst2=list(map(int,input("Enter numbers in LIST 2 with spaces in between: ").split()))
print(f"list 1: {lst1}")
print(f"list 2: {lst2}")

mrge = lst1+lst2
print(f"the merge of list 1 and 2 : {mrge}")
sorted_lst=[]

while mrge:
    smallest = mrge[0]

    for num in mrge:
        if num < smallest:
            smallest=num

    sorted_lst.append(smallest)
    mrge.remove(smallest)

print(f"the sorted list: {sorted_lst}")        
        






        






