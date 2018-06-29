# Generate Gitfiles
generate:
  mkdir files
  git clone https://github.com/github/gitignore.git
  git clone https://github.com/alexkaratarakis/gitattributes.git
  python generate.py $PWD
  rm -rf gitignore
  rm -rf gitattributes
# Generate Gitfiles with a Dirfile to specify directory
generatewithdir: Dirfile.txt
  mkdir files
  git clone https://github.com/github/gitignore.git
  git clone https://github.com/alexkaratarakis/gitattributes.git
  python generate.py line=$(head -n 1 filename)
  rm -rf gitignore
  rm -rf gitattributes
  
