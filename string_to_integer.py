




ps="ik  +-4 289 ik"

import re
l = list([int(float(s)) for s in re.findall(r'-?\d+\.?\d*', ps)])
print(l)
if l:
    print(l[0])
else:
    print(0)
