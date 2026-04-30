#find all the pairs in the list whos sum is equal to the target

def two_sum(nums,target):
    new_map={}

    for i, num in enumerate(nums):
        current = target-num
        
        if current in new_map:
            return [nums[new_map[current]],num]        
        new_map[num]=i

    return

print(two_sum([1,2,4,6,5,3],9))
