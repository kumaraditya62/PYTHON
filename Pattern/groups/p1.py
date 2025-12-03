import re
pattern =r"gr(ea)*t"
if re.match(pattern, "great"):
    print("Match ea")
if re.match(pattern, "greaeaeaeaeat"):
    print("Match greaeaeaeaeat")