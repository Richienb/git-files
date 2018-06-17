# Clear files
print("Clearing files...")
open("files/.gitignore", "w").close()
open("files/.gitattributes", "w").close()

# Search for all gitignore files and append them to a list
print("Searching for all .gitignore files...")
ignorefile = []
import glob, os
os.chdir("gitignore")
for file in glob.glob("*.gitignore"):
    ignorefile.append(file)

# Merge all the gitignore files into one file
print("Merging all .gitignore files...")
for i in enumerate(ignorefile):
    f = open("files/.gitignore", "w")
    f.write(i[1].read())
    
# Search for all gitattributes files and append them to a list
print("Searching for all .gitattributes files...")
attributefile = []
import glob, os
os.chdir("gitattributes")
for file in glob.glob("*.gitattributes"):
    if not file == ".gitattributes":
        ignorefile.append(file)
        
# Merge all the gitattributes files into one file
print("Merging all .gitattributes files...")
for i in enumerate(attributefile):
    f = open("files/.gitattributes", "w")
    f.write(i[1].read())
