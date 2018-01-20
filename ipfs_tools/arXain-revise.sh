#!/bin/bash

while getopts f:d: option
do
	case "${option}"
	in
	f)	DIRECTORY=${OPTARG};;
	d)	DOI=${OPTARG};;
	esac
done

# Get the confi settings
cd ~/arXain-repo

. ./config

#Calculate the save directory
paperDirectory="${DOI}"

cd "${authorID}"

mkdir "${paperDirectory}"

numVersions=$(find ${paperDirectory}/ -type d -maxdepth 1 | wc -l)
numVersions=$(echo ${numVersions//[[:blank:]]/})

cd "$paperDirectory"
mkdir v"$numVersions"
cd v"$numVersions"
targetDirectory=$(pwd)

cp -a $DIRECTORY. $targetDirectory

# Add the latest version to IPFS and get the hash
CORPUS_HASH=$(ipfs add -r -Q ${targetDirectory})

echo "Revision v${numVersions} of ${paperDirectory} hashed to ${CORPUS_HASH}"
echo "AuthorID ${authorID}"
