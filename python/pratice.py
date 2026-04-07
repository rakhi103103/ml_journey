# Q------------------Q1 – Find First Non-Repeating Character---------------------------
arr = input("enter the word: ")
print(f"The word is {arr}")
for char in arr:
    if arr.count(char)==1:
        print(f"The first non-repetaing letter is {char}")
        break
        

# Q------------------Q2 – Flatten Nested List-------------------------------
def flatten(nums):
    result =[]
    for items in nums:
        if isinstance(items,list):
            result.extend(flatten(items))
        else:
            result.append(items)
    
    return result

num = [1,2,[3,4],5,[6,[7,8,9],10]]

print(flatten(num))

# Q--------------Q3 – Group Anagrams------------
wordd=["eat","tea","tan","ate","nat","bat"]
group = {}

for word in wordd:
    key = "".join(sorted(word))

    if key not in group:
        group[key]=[]

    group[key].append(word)
print(list(group.values()))

# Q------------Q4 – Find Missing Number------------------

ls = int(input("Enter len of array: "))
arra=[]
for i in range(ls):
    num = int(input(f"enter the element in the array: "))
    arra.append(num)


n = len(arra)+1
expected_sum = n*(n+1)//2
actual_sum = sum(arra)

missing_value = expected_sum - actual_sum

print(f"The misising value is {missing_value}")


# Q---------------Q5 – Most Frequent Word---------------------
text = input("Enter the words: ")
words = text.split()
freq={}

for i in words:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

max_word = max(freq, key=freq.get)

print(f"Most Frequent Word is {max_word}")

# Q---------------Q6 – Check Balanced Parentheses-----------------------------------
def check(s):
    stack = []

    pairs={
        ")":"(",
        "}":"{",
        "]":"["
    }
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack == [] or stack[-1]!=pairs[char]:
                return False
            stack.pop()
    return stack

text=input("Enter the parentheses string: ")

print(check(text))



 
