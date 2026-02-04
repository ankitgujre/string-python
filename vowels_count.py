st = input("Enter string: ")

count = 0
for ch in st:
    if ch in "aeiouAEIOU":
        count += 1
    else:
        print("consonant")

print("Total vowels =", count)
