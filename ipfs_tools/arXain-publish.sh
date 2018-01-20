#!/bin/bash


# Hash the repository and grab it
REPO_HASH=$(ipfs add -r -Q ~/arXain-repo)

# Publish the repository with the arXain-key
echo "Generating... please be patient."
OUTPUT=$(ipfs name publish --key=arXain-key /ipfs/$REPO_HASH)

echo "$OUTPUT"