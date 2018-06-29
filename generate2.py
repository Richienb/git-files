from sys import argv as args
from pprint import pprint
import glob, os

# Set root directory
try:
    rootdir = args[1]
except:
    print("Please specify the directory you are running this script in.")

# Clear files
print("Clearing files...")
open("files/.gitignore", "w").close()
open("files/.gitattributes", "w").close()

# Search for all gitignore files and append them to a list
print("Searching for all .gitignore files...")
ignorefile = []
os.chdir("{}/gitignore".format(rootdir))
for file in glob.glob("*.gitignore"):
    ignorefile.append(file)
print("Found .gitignore files:")
pprint(ignorefile)

# Merge all the gitignore files into one file
print("Merging all .gitignore files...")
with open("{}/files/.gitignore".format(rootdir), "a+") as f:
    for i in enumerate(ignorefile):
        with open("{}/gitignore/{}".format(rootdir, i[1])) as ff:
            for ii in enumerate(ff.readlines()):
                f.write(str(ii[1]))
    print(".gitignore contents: ")
    pprint(f.readlines())
    
# Search for all gitattributes files and append them to a list
print("Searching for all .gitattributes files...")
attributefile = []
os.chdir("{}/gitattributes".format(rootdir))
for file in glob.glob("*.gitattributes"):
    if not file == ".gitattributes":
        ignorefile.append(file)
print("Found .gitattributes files:")
pprint(attributefile)
        
# Merge all the gitattributes files into one file
print("Merging all .gitattributes files...")
with open("{}/files/.gitattributes".format(rootdir), "a+") as f:
    for i in enumerate(attributefile):
        with open("{}/gitattributes/{}".format(rootdir, i[1])) as ff:
            for ii in enumerate(ff.readlines()):
                f.write(str(ii[1]))
    print(".gitattributes contents: ")
    pprint(f.readlines())
