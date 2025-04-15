def gen_perm(s, cur =""):
    if len(s) == 0:
        print(cur)
        return 0
    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]
        gen_perm(remaining, cur + s[i])

string = input("Enter a string: ")
print(gen_perm(string))