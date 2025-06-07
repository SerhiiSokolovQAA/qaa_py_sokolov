data_to_ckeck = input("Enter your data: ")
#Solution #1
unique_chars = []
for char in data_to_ckeck:
    if char not in unique_chars:
        unique_chars.append(char)
if len(unique_chars) > 10:
    print(True)
else:
    print(False)

#Solution #2
unique_chars = set(data_to_ckeck)
print(len(unique_chars) > 10)