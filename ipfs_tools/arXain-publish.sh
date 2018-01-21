#!/bin/bash

ETH_ADDRESS="$@"

# Hash the repository and grab it
REPO_HASH=$(ipfs add -r -Q ~/arXain-repo/${ETH_ADDRESS})

# Publish the repository with the arXain-key
echo "Generating... please be patient."
OUTPUT=$(ipfs name publish --key=arXain-${ETH_ADDRESS} /ipfs/$REPO_HASH)

echo "$OUTPUT"