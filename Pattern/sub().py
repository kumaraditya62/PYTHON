import re
string ="She sells seashells by the seashore."
pattern ="sea"
repl = "ocean"
new_string = re.sub(pattern, repl, string,1)
print(new_string)  