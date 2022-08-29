import os
import re


for name in os.listdir(r"D:\Test_folder"):
    c_name = re.search(r"(^\w+)(?: ?\(\d\)| - Copy.*)\.\w+$", name, re.IGNORECASE)
    if c_name:

        # Compare clear name with next 5 names
        for i in range(5):

        print(c_name.group(1))