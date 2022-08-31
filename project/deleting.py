from msilib.schema import Directory
import os
import re




def analyze(directory):

    f_list = os.listdir(directory)
    remove_list = []
    rename_list = []

    for i, name in enumerate(f_list):

        # Peel the file name
        s_name = strip(name)
        if s_name != name:
            removed = False

            # Compare stripped name with next 5 names
            for j in range(1, 6):

                try: # try-except to avoid out of index error        
                    if s_name == strip(f_list[i + j]):
                        # size comparison ==========================
                        if os.path.getsize(directory + "\\" + name) == os.path.getsize(directory + "\\" + f_list[i + j]):     
                            remove_list.append(name)
                            removed = True
                except:
                    break

            # If nothing was removed, just rename
            if not removed:
                rename_list.append(name)
    
    return remove_list, rename_list


def strip(name):
    if s_name := re.search(r"(^\w+)(?: ?\(\d+\)| - Copy.*)(\.\w+)$", name, re.IGNORECASE):
        return s_name.group(1) + s_name.group(2)
    else:
        return name


def remove(directory, remove_list):
    for name in remove_list:
        os.remove(directory + "\\" + name)


def rename(directory, rename_list):
    for name in rename_list:
        os.rename(directory + "\\" + name, directory + "\\" + strip(name))


def main(directory):
    remove_list, rename_list = analyze(directory)
    remove(directory, remove_list)
    rename(directory, rename_list)


if __name__ == "__main__":
    main(r"D:\Test_folder")
