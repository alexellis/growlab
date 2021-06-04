#!/bin/bash
python3 app.py

export GIT_SSH_COMMAND="ssh -i `pwd`/.ssh/id_rsa"

cp ${HOME}/growlab/app/html/* ${HOME}/growlab/docs/
cd ${HOME}/growlab
git add .
echo "commit ..."
git commit -s -m "Update images at `date`"
echo "pull ..."
pwd
git pull origin master --rebase
echo "push ..."
git push origin master

