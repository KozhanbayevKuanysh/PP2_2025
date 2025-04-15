def spy_game(nums):
    agent_007 = [0, 0, 7]
    index = 0
    for i in nums:
        if i == agent_007[index]:
            index += 1
            if index == len(agent_007):
                print("True")
                return 0
    print("False")
    return 0

spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0]) 