#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git checkout -b gh-pages
  git add $PWD/files/.gitignore
  git add $PWD/files/.gitattributes
  git commit --message "Updated Git Files"
}

upload_files() {
  git remote add origin-pages https://${GH_TOKEN}@github.com/Richienb/git-files.git > /dev/null 2>&1
  git push origin master
}

setup_git
commit_files
upload_files
