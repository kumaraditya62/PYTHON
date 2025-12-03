import re
pattern = r"hi(de)+"
if re.search(pattern, "hidedede"):
    print("Match hidedede")
if re.search(pattern, "hi"):
    print("Match hi")
