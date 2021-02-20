import glob
import os

print (os.getcwd())
f_name = "7.md"
f_path = os.path.join(os.getcwd(),f_name)
print (f_path)

file_data = ""

with open (f_path, "r", encoding='utf-8') as f:
    for line in f:
        if ("\\" not in line) and ("***" not in line):
            line = line[:-1]+"\\"+line[-1]
        file_data = file_data + line


with open(f_path,"w",encoding="utf-8") as f:
        f.write(file_data)
