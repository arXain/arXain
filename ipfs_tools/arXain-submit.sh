#!/bin/bash

while getopts a:f:d: option
do
	case "${option}"
	in
	a)	authorID=${OPTARG};;
	f)	DIRECTORY=${OPTARG};;
	d)	DOI=${OPTARG};;
	esac
done

# Get the confi settings
cd ~/arXain-repo/"${authorID}"/manuscripts

numPapers=$(find . -type d -maxdepth 1 | wc -l)
numPapers=$(echo ${numPapers//[[:blank:]]/})


#Calculate the save directory
paperDirectory="${authorID}_${numPapers}"



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

echo "Initial submission of ${paperDirectory} hashed to ${CORPUS_HASH}"
echo "DOI ${DOI}"



