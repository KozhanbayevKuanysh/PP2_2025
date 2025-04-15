def find_unique(nums):
    uniques = []
    
    for i in range(len(nums)):
        if nums[i] not in uniques:
            uniques.append(nums[i])
    print(uniques)
    print(set(nums))

find_unique([3, 5, 6, 1, 10, 32, 3, 6, 8, 3, 12, 31, 5, 11])