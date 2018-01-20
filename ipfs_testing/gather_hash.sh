#!/bin/bash

localdirec="http://localhost:8080/ipfs/"
gway="http://ipfs.io/ipfs/"

for FILE in "$@"
do
	hash=$(ipfs add -r -Q $FILE) # | tail -n1); \
	echo "Hash added to" "$output" 
	echo "View this directory @:"
    echo "$localdirec""$hash" 
    echo "$gway""$hash"
done