

with open ('lol.txt', 'rt') as myfile:
    contents = myfile.read()              
print(contents)

if "Diane" in contents:
    print("There is Poppy")
else:
    print("RIP")
        