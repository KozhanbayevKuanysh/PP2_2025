def polindrome(str):
    for i in range(len(str) // 2):
        if str[i] != str[-(i + 1)]:
            print("False")
            return 0
    print("True")
    return 0

polindrome("LEGENDARY")
polindrome("madam")