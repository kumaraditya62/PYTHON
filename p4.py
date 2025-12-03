#program that uses different methods (uppercase, lowercase, split, count, replace, and find on) string object.
str ="Welcome to the world of Python programming"
print("uppercase:", str.upper())
print("lowercase:", str.lower())
print("split:", str.split())
print("count of 'o':", str.count('o'))
print("replace 'Python' with 'Java':", str.replace('Python', 'Java'))
print("join ", '-'.join(str.split()))
print("find of", str.find('of'))