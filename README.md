# Git Files [![Travis CI Status](https://img.shields.io/travis/Richienb/git-files.svg?style=for-the-badge)](https://travis-ci.org/Richienb/git-files)

A `.gitignore` and `.gitattributes` file containing ignore and attribute code for all programming languages, automatically updated daily.

## How to use

Execute the commands while in the root directory of your Git repository

- [From URL](#from-url)
- [Using Makefile](#using-makefile)
- [Using cURL](#using-curl)
- [Using wGET](#using-wget)
- [Using Traditional Git Cloning](#using-traditional-git-cloning)

### From URL:

```
https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

### Using Makefile:

#### Pull from repository

```sh
make pull
```

#### Generate the files

```sh
make generate
```

### Using cURL:

```sh
$ curl -L -o .gitignore https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
$ curl -L -o .gitattributes https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

### Using Wget:

```sh
$ wget https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
$ wget https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

### Using traditional Git cloning:

```sh
$ git clone https://github.com/Richienb/git-files.git
$ mv -f git-files/files/.gitignore .
$ mv -f git-files/files/.gitattributes .
$ rm -rf git-files
```

### Generate the files yourself

```sh
mkdir -p files
git clone https://github.com/github/gitignore.git
git clone https://github.com/alexkaratarakis/gitattributes.git
python generate.py $PWD
rm -rf gitignore
rm -rf gitattributes
```
