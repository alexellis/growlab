#!/bin/bash
python3 app.py

export GIT_SSH_COMMAND="ssh -i `pwd`/.ssh/id_rsa"

cp html/* ./growlab-live/docs/
cd growlab-live

git add .

git commit -s -m "Update images at `date`"
git pull origin master --rebase
git push origin master

