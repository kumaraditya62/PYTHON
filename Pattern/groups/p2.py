import re
pattern = r"Go(od)Go(in)gpy(th)on"
match = re.search(pattern, "GoodGoingpythonGoodGoingpythonGoodGoingpython")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())