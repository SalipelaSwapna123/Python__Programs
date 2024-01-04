s=input("Enter a string : ")
s=s.lower()
unique_letters = []
for ch in s:
    if ch not in unique_letters:
        unique_letters.append(ch)
l=','.join(unique_letters)
print(l)