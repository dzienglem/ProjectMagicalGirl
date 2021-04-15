import glob
import os

print (os.getcwd())
num = 1
symb = "\\"
f_name = "{}.md".format(num)
f_path = os.path.join(os.getcwd(),f_name)
print (f_path)

file_data = ""

with open (f_path, "r", encoding='utf-8') as f:
    for line in f:
        if (symb not in line) and ("***" not in line):
            line = line[:-1]+symb+line[-1]
        elif "***" in line:
            print ("*** is found")
            while symb in file_data[-2:]:
                print ("delete symb")
                file_data = file_data[:-1]
            file_data = file_data + "\n"
        file_data = file_data + line

if file_data[-2] != ")":
    print (file_data[-2])
    file_data = file_data + "[Next]({}.md) ".format(num+1)

with open(f_path,"w",encoding="utf-8") as f:
        f.write(file_data)
