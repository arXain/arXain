# How to interact with the IPFS end of arXain

## 
Make sure that you have the latest branch of arXain and are in the arXain/ipfs_tools directory

After knowing your author ID (which should be your ethereum wallet address), initialize the local repository that papers and reviews will go into.

``
./arXain-init.sh <insert-ether-address>
``

You will get  reponse with your peer ID. Write down this hash and keep it safe, as it will allow people to access your directory of papers and reviews through /ipns/<peerID>, even after you have updated the files and the hash changes. The files are initialized in the home directory at ~/arXain-repo. Here you can find a config file that shows your peer ID and your authorID should you forget them.

## Submitting an article
Create a directory with the following contents

``
meta.json
<insert-ether-address>_paperNumber.pdf
``

The <ether-address>_paperNumber acts as our digital object identifier (DOI)
The json should have the following keys:

``
title : string,
authors : string (Last1, First1; Last2, First2; ...)
abstract : string
tags : array of strings
timestamp: string in javascript date format ("Month DD, YYYY HH:MM:SS")
doi : string <insert-ether-address>_paperNumber
submitter : <insert-ether-address>
revision : 1
reviewStatus : vector of bools
``

Make a note of the full path of your repository, and run the submit script

``
david$./arXain-submit.sh /path/to/folder/for/submission/
``

This will make a folder corresponding to this DOI in your ~/arXain-repo and add it as the first version. The article directory hash and authorID will be output to the console so that you can enter it into the ipfs web interface with the blockchain. Example output for an authorID of 0x12345 and the first paper submitted is below

``
david$ ./arXain-submit.sh ~/arXain/ipfs_tools/genesis-article/
0x12345_1/v1/ hashed to QmZxcRoU6mqdarzaNTxakXDz58CkivSJ4YHfvFgKHzagyX
AuthorID 0x12345
``

## Publishing your article for more permanance on the network
Publish your complete respository such that someone viewing our author page (given by /ipns/<peerID>) can see the latest submission. This command can take a bit of time to run. Exmple output is shown.

``
david$./arXian-publish.sh
Generating... please be patient.
Published to QmZtAAiQk93eM9mgyirwZHSk7rYoatus5C9SToVq4CxxB5: /ipfs/QmZ7Lg3752Vh7L7A32JdbZEiT7DSc9DGfWvZ6UEUXevAWy
``

Directing your ipfs browser to ``/ipns/QmZtAAiQk93eM9mgyirwZHSk7rYoatus5C9SToVq4CxxB5`` now lets you see your submission.

