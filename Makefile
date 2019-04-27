# Generate Gitfiles
generate:
	mkdir -p files
	git clone https://github.com/github/gitignore.git
	git clone https://github.com/alexkaratarakis/gitattributes.git
	python generate.py $PWD
	rm -rf gitignore
	rm -rf gitattributes

# Pull Gitfiles from repository
pull:
	git clone https://github.com/Richienb/git-files.git
	mv -f git-files/files/.gitignore .
	mv -f git-files/files/.gitattributes .
	rm -rf git-files
