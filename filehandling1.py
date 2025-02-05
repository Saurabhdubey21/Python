import os
current_dir=os.getcwd
print(current_dir)
os.chdir("C:\Program Files (x86)")
print("changed directory",os.getcwd())
os.mkdir("life")
contents=os.listdir(".")
print("dictionary contents:",contents)
os.rmdir("life")