str = input("Input: ")
new_string = []
for char in str:
    if char not in 'aeiouAEIOU':
        new_string.append(char)
print(f"Output: {''.join(new_string)}")



