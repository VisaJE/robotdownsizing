#!/bin/bash
git add -A
git commit -m "Automated message, ignore"
git pull origin master --rebase
git push origin master
