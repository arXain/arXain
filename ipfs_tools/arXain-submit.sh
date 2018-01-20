#!/bin/bash

DIRECTORY="$@"

# Get the confi settings
cd ~/arXain-repo

. ./config

numPapers=$(find ${authorID}/ -type d -maxdepth 1 | wc -l)
numPapers=$(echo ${numPapers//[[:blank:]]/})


#Calculate the save directory
paperDirectory="${authorID}_${numPapers}"

cd "$authorID"

mkdir "$paperDirectory"


numVersions=$(find ${paperDirectory}/ -type d -maxdepth 1 | wc -l)
numVersions=$(echo ${numVersions//[[:blank:]]/})

cd "$paperDirectory"
mkdir v"$numVersions"
cd v"$numVersions"
targetDirectory=$(pwd)

cp -a $DIRECTORY. $targetDirectory

# Add the latest version to IPFS and get the hash
CORPUS_HASH=$(ipfs add -r -Q ${targetDirectory})

echo "${paperDirectory}/v${numVersions}/ hashed to ${CORPUS_HASH}"
echo "AuthorID ${authorID}"



