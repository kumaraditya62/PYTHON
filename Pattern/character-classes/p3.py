#wap to demo the use of {m,n} regular expression
import re
pattern = r"2{1,4}$"
if re.search(pattern, "2"):
    print("Match 2")
if re.search(pattern, "222"):
    print("Match 222")
if re.search(pattern, "22222"):
    print("Match 22222")