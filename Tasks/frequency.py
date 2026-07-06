print("Counting frequency of characters in a string")
word = input("Enter a string: ")
frequency = {}
for char in word:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequency in the string:")
for char, count in frequency.items():
    print(f"{char}: {count}")
