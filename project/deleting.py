import os
import re


dir = r"D:\Test_folder"


def analyze(dir):

    f_list = os.listdir(dir)
    remove_list = []
    rename_list = []

    for i, name in enumerate(f_list):
        if s_name := shorten(name):
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
                rename_list.append(name)
                    
    return remove_list, rename_list


def shorten(name):
    s_name = re.search(r"(^\w+)(?: ?\(\d+\)| - Copy.*)(\.\w+)$", name, re.IGNORECASE)
    if s_name:
        return s_name.group(1) + s_name.group(2)


def remove(remove_list):
    for name in remove_list:
        os.remove(dir + "\\" + name)


def rename(rename_list):
    for name in rename_list:
        s_name = shorten(name)
        os.rename(dir + "\\" + name, dir + "\\" + s_name)


def main():
    remove_list, rename_list = analyze(dir)

    print("Remove:")
    for name in remove_list:
        print(name)
    remove(remove_list)

    print("Rename:")
    for name in rename_list:
        print(name)
    rename(rename_list)




if __name__ == "__main__":
    main()