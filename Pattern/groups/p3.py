#named and noncapturing groups
import re
pattern = r"Go(?P<first>od)Go(?:in)gpy(th)on"
match = re.match(pattern, "GoodGoingpythonGoodGoingpythonGoodGoingpython")
if match:
    print(match.group("first"))
    print(match.group(1))
    print(match.group(2))
    print(match.group())