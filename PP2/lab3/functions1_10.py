def find_unique(nums):
    uniques = []
    for i in nums:
        if i not in uniques:
            uniques.append(i)
    print(uniques)

find_unique([3, 5, 6, 1, 10, 32, 3, 6, 8, 3, 12, 31, 5, 11])