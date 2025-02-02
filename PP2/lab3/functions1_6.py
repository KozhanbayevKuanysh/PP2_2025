def reverse_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed = ' '.join(words[::-1])
    return reversed

print(reverse_words())