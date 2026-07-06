print("Reversing the word")
sentence = str(input("Give your word i will reverse: "))
sentence = sentence.split()
rev = []
result = ""
for word in sentence:
     rev.append(word[::-1])
for rev_word in rev:
     result = result + rev_word + " "
print(result)

