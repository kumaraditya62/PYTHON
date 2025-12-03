import re
pattern =r"[a-zA-Z]+\s*\d+"
matches = re.findall(pattern, "LXI 2013, VXI 2015, VDI 2014, Maruti suzuki cars in india")
for match in matches:
    print(match,end=" ")