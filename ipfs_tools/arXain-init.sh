#!/bin/bash

ETH_ADDRESS="$@"

cd ~/

mkdir arXain-repo
cd arXain-repo

mkdir "$ETH_ADDRESS"
mkdir reviews


cd ..

# Create a unique public key for arXain to host at
KEYS=$(ipfs key list)
ALLOWED="arXain-key"

echo ${KEYS} | grep --quiet "${ALLOWED}"

if [ $? = 1 ]
then
	echo "arXain specific key not found, generating..."

	#Create a unique key for hosting the arXain repository
	PUBLIC_KEY=$(ipfs key gen --type=rsa --size=2048 arXain-key)

	echo "added $PUBLIC_KEY key=arXain-key"
else
	ALL_KEYS=$(ipfs key list -l)
	PUBLIC_KEY=$(echo $ALL_KEYS | grep -Eo "([a-zA-Z0-9]+)( arXain-key)" | grep -Eo "([a-zA-Z0-9]+)" | head -1)

	echo "peerID found @ $PUBLIC_KEY"
fi

cd arXain-repo

# set up config file for easily accessing stuff
printf '#!/bin/bash\n\nauthorID="%s"\npeerID="%s"\n' "$ETH_ADDRESS" "$PUBLIC_KEY" > config.sh

chmod u+x config.sh
