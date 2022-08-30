import os
import re


dir = r"D:\Test_folder"


def analyze(dir):
    
    f_list = os.listdir(dir)
    remove_list = []

    for i, name in enumerate(f_list):

        # Peel the file name
        if s_name := re.search(r"(^\w+)(?: ?\(\d+\)| - Copy.*)(\.\w+)$", name, re.IGNORECASE):
            s_name = s_name.group(1) + s_name.group(2)
            removed = False

            # Compare stripped name with next 5 names
            for j in range(1, 6):

                try: # try-except to avoid out of index error
                    if s_name == f_list[i + j]:

                        # size comparison ==========================
                        if os.path.getsize(dir + "\\" + name) == os.path.getsize(dir + "\\" + f_list[i + j]):     
                            remove_list.append(name)
                            removed = True
                except:
                    break

            # If nothing was removed, just rename
            if not removed:
                os.rename(dir + "\\" + name, dir + "\\" + s_name)
    
    return remove_list


def remove(remove_list):
    for name in remove_list:
        os.remove(dir + "\\" + name)



def main():
    
    remove_list = analyze(dir)
    remove(remove_list)






if __name__ == "__main__":
    main()