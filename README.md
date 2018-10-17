# Git Files [![Travis CI Status](https://img.shields.io/travis/Richienb/git-files.svg?style=for-the-badge)](https://travis-ci.org/Richienb/git-files)

A `.gitignore` and `.gitattributes` file containing ignore and attribute code for all programming languages, automatically updated daily.

## How to use

Execute the commands while in the root directory of your Git repository

- [From URL](#method-1---from-url)
- [Using cURL](#method-2---using-curl)
- [Using wGET](#method-3---using-wget)
- [Using Traditional Git Cloning](#method-4---using-traditional-git-cloning)

### Method 1 - From URL:

```
https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

### Method 2 - Using cURL:

#### Travis CI
```yml
install:
  - curl -L -o .gitignore https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
  - curl -L -o .gitattributes https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

#### Shell/Terminal
```sh
$ curl -L -o .gitignore https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
$ curl -L -o .gitattributes https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

#### Cmd/Batch/Powershell
```bat
curl -L -o .gitignore https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
curl -L -o .gitattributes https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

### Method 3 - Using Wget:

#### Travis CI
```yml
install:
  - wget https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
  - wget https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

#### Shell/Terminal
```sh
$ wget https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
$ wget https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

#### Cmd/Batch/Powershell
```bat
wget https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitignore
wget https://raw.githubusercontent.com/Richienb/git-files/master/files/.gitattributes
```

### Method 4 - Using traditional Git cloning:

#### Travis CI
```yml
install:
  git clone https://github.com/Richienb/git-files.git
  mv -f git-files/files/.gitignore .
  mv -f git-files/files/.gitattributes .
  rm -rf git-files
```

#### Shell/Terminal
```sh
$ git clone https://github.com/Richienb/git-files.git
$ mv -f git-files/files/.gitignore .
$ mv -f git-files/files/.gitattributes .
$ rm -rf git-files
```

#### Cmd/Batch/Powershell
```bat
git clone https://github.com/Richienb/git-files.git
move /Y git-files/files/.gitignore .
move /Y git-files/files/.gitattributes .
rmdir -S -Q git-files
```
