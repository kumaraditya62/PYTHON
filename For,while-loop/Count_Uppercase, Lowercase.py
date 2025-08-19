ch = input("Enter any character: ")
num_count = 0
up_count = 0
low_count = 0

while(ch != '*'):
    if '0' <= ch <= '9':
        num_count += 1
    elif 'a' <= ch <= 'z':
        low_count += 1
    elif 'A' <= ch <= 'Z':
        up_count += 1
    
    ch = input("Enter any character: ")

print("Total count of numerals entered =", num_count)
print("Total count of lowercase characters entered =", low_count)
print("Total count of uppercase characters entered =", up_count)
