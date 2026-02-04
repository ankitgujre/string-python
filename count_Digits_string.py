st = input("Enter string: ")

count = 0

for ch in st:
    if ch >= '0' and ch <= '9':
        count += 1

print("Total digits =", count)
