#!/bin/bash

python3 app.py
cp html/* ../docs/

git add ..
git commit -s -m "Update images at `date`"
GIT_SSH_COMMAND="ssh -i `pwd`/.ssh/id_rsa" git pull origin master --rebase
GIT_SSH_COMMAND="ssh -i `pwd`/.ssh/id_rsa" git push origin master

