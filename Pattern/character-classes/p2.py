import re
pattern = r"hi(de)*"
if re.search(pattern, "hidededededede"):
    print("Match hidededededede")
if re.search(pattern, "hi"):
    print("Match hi")