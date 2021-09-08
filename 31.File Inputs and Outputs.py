import os

print("Hello World")

#var1 = input("Enter something please: ")
#print(var1)

var2 = open("file.txt", "r+")
print(var2)
print(var2.name)





#var2.write("Hello My Name Is Bob")

string1 = var2.read(12)

print(string1)


var2.close()

#os.rename("file.txt", "New Name.txt")
#os.remove("Filelocalion and filename")
#os.mkdir("New Folder")
