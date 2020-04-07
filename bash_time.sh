#!/bin/bash

# start with what we know, then move on to more complicatesd tasks

VAR=$(date +"%FORMAT_STRING")
NOW=$(date +"%m_%d_%Y")
printf "%s is right now saved in this machines shell\n" $NOW
TODAY=$(date +"%Y-%m-%d")
printf "Today we are going to backup file to NFS server at AWS '%s'\n" "/efs/my-blog-${TODAY}.sql.tar.gz"