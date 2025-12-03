#wap to demo the use of metacharacters and groups.
import re
match = re.search("([0-9]+).*:(.*)"," phone number:12345678, DOB:october 2, 2000")
if match:
    print(match.group())
    print(match.group(1)) 
    print(match.group(2)) 
    print(match.group(1,2)) 