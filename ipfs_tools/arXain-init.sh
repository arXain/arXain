#!/bin/bash

ETH_ADDRESS="$@"

cd ~/

mkdir arXain-repo
cd arXain-repo

mkdir "$ETH_ADDRESS"
cd "$ETH_ADDRESS"
mkdir manuscripts
mkdir reviews


cd ..

# Create a unique public key for arXain to host at
KEYS=$(ipfs key list)
ALLOWED="arXain-${ETH_ADDRESS}"

echo ${KEYS} | grep --quiet "${ALLOWED}"

if [ $? = 1 ]
then
	echo "arXain specific key not found, generating..."

	#Create a unique key for hosting the arXain repository
	PUBLIC_KEY=$(ipfs key gen --type=rsa --size=2048 arXain-${ETH_ADDRESS})

	echo "added $PUBLIC_KEY key=arXain-${ETH_ADDRESS}"
else
	ALL_KEYS=$(ipfs key list -l)
	PUBLIC_KEY=$(echo $ALL_KEYS | grep -Eo "([a-zA-Z0-9]+)( arXain-${ETH_ADDRESS})" | grep -Eo "([a-zA-Z0-9]+)" | head -1)

	echo "peerID: $PUBLIC_KEY"
fi

cd ~/arXain-repo/"${authorID}"/
# set up config file for easily accessing stuff
printf '\nauthorID="%s"\npeerID="%s"\n' "$ETH_ADDRESS" "$PUBLIC_KEY" > config.txt

