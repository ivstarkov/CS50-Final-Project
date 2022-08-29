import os
import re


dir = r"D:\Test_folder"
f_list = os.listdir(dir)
for i, name in enumerate(f_list):
    s_name = re.search(r"(^\w+)(?: ?\(\d+\)| - Copy.*)(\.\w+)$", name, re.IGNORECASE)
    
    if s_name:
        s_name = s_name.group(1) + s_name.group(2)
        
        # Compare stripped name with next 5 names
        for j in range(1, 6):
            try:
                if s_name == f_list[i + j]:
                    # TODO: size and header comparison 
                    os.remove(dir + "\\" + name)
            except:
                break

