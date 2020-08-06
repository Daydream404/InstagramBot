'''with open ('lol.txt', 'rt') as myfile:
    contents = myfile.read()              
print(contents)

if "Diane" in contents:
    print("There is Poppy")
else:
    print("RIP")
        

list = ['Daniel','lol', 'lol1']
print(type(list))

if "Daniel" in list:
    print("DID")
else:
    print("RIP")

'''


import instaloader

instg = instaloader.Instaloader()
PROFILE = "discordpy"
instg.login("discordpy", "iMCXcu9zAbjE")
profile = instaloader.Profile.from_username(instg.context, PROFILE)

open('lol.txt', 'w').close()

file = open("lol.txt","a+")
for flwrs in profile.get_followees():
    username = flwrs.username
    file.write(username + "\n")
    print(username)

file.close()

with open ('lol.txt', 'rt') as myfile:
    contents = myfile.read()              


if "pycoders" in contents:
    print("There is Poppy")
else:
    print("RIP")