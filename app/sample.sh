#!/bin/bash
python3 app.py

export GIT_SSH_COMMAND=""

cp ${HOME}/growlab/app/html/* ${HOME}/growlab/docs/
cd ${HOME}/growlab
git add .

git commit -s -m "Update images at `date`"
git pull origin master --rebase
git push origin master

