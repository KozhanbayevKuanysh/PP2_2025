def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            print("True")
            return 0
    print("False")
    return 0

def polindrome(str):
    for i in range(len(str) // 2):
        if str[i] != str[-(i + 1)]:
            print("False")
            return 0
    print("True")
    return 0

def vol_of_sphere(radius):
    volume = (4/3) * 3.14 * radius**3
    print(volume)