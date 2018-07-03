# Generate Gitfiles
generate:
	mkdir -p files
	git clone https://github.com/github/gitignore.git
	git clone https://github.com/alexkaratarakis/gitattributes.git
	python generate.py $PWD
	rm -rf gitignore
	rm -rf gitattributes
