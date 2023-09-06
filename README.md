# Hari-Anna


"""

E: folder is from the pendrive  
```python
"""

import os
os.chdir("E:")
p = []
cpu = []
mon = []
for i in os.listdir("."):
    if os.path.isdir(i):
        if "sys" in i:
#             print(i)
            for j in os.listdir(os.path.join(os.getcwd(),i)):
#                 print(j)
                if "cpu" in os.path.join(os.getcwd(),i,j):
                    with open(os.path.join(os.getcwd(),i,j),"rb") as f:
                        D = f.read()
                    s = D.decode('utf-16le', 'ignore')
                    s = s.replace("\n","").replace("\r","").strip().split()[-1]
#                     print(s)
                    p.append(i)
                    cpu.append(s)
                else:
                    with open(os.path.join(os.getcwd(),i,j),"r") as f1:
                        data = f1.read().strip()
                    mon.append(data)
#                     print(data)      
import pandas as pd
df = pd.DataFrame([p,cpu,mon]).T
df.columns = ["Systems","CPU_srial_num","Monitor_serial_num"]
df.to_excel("sys_info.xlsx",index=False)
df

```
