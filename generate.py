from sys import argv as args
import glob, os

# Set root directory
rootdir = args[1]

# Clear files
print("Clearing files...")
open("files/.gitignore", "w").close()
open("files/.gitattributes", "w").close()

# Search for all gitignore files and append them to a list
print("Searching for all .gitignore files...")
ignorefile = []
os.chdir("gitignore")
for file in glob.glob("*.gitignore"):
    ignorefile.append(file)

# Merge all the gitignore files into one file
print("Merging all .gitignore files...")
f = open("{}/.gitignore".format(rootdir), "a+")
for i in enumerate(ignorefile):
    f.write(i[1])
f.close()
    
# Search for all gitattributes files and append them to a list
print("Searching for all .gitattributes files...")
attributefile = []
os.chdir("gitattributes")
for file in glob.glob("*.gitattributes"):
    if not file == ".gitattributes":
        ignorefile.append(file)
        
# Merge all the gitattributes files into one file
print("Merging all .gitattributes files...")
f = open("{}/.gitattributes".format(rootdir), "a+")
for i in enumerate(attributefile):
    f.write(i[1])
f.close()
