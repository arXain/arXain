<div style="text-align: center;"><img src="https://github.com/david-hopper/arXain/blob/master/src/images/logo_name.png" alt="arXain" /></div>

## Inspiration

Peer-review science is critical to modern science, engineering, and healthcare 
endeavors. However, the system for implementing this process has lagged behind 
and results in expensive costs for publishing and accessing material, long turn 
around times reminiscent of snail-mail, and shockingly opaque editorial 
practices. Astronomy, Physics, Mathematics, and Engineering using a "pre-print 
server" ([arXiv](https://arxiv.org)) which was the early internets improvement 
upon snail-mailing articles to researchers around the world. This pre-print 
server is maintained by a single University, and is constantly requesting 
donations to keep up the servers and maintenance. While researchers widely 
acknowledge the importance of the pre-print server, there is no peer-review 
incorporated, and none planned due to technical reasons. Thus, researchers are 
stuck with spending >$1000 per paper to be published in Journals, all the while 
individual article access can cost as high as $32 per paper! 
([source](https://www.nature.com/subscriptions/purchasing.html)). For reference, 
a single PhD thesis can contain >150 references, or essentially cost $4800 if 
purchased individually.

The recent advance of blockchain and smart contract technology 
([Ethereum](https://www.ethereum.org/)) coupled with decentralized 
file sharing networks ([InterPlanetaryFileSystem](https://ipfs.io)) 
naturally lead us to believe that archaic journals and editors could 
be bypassed. We fashioned our manuscript distribution and reviewing 
platform based on the arXiv, but in a completely decentralized manner. 
Users utilize, maintain, and grow the network of scholarship by simply 
running a simple program and web interface.


## What it does

arXian deals with all the aspects of a peer-reviewed journal service.
An author (wallet address) will come with a bomb-ass paper they wrote. 
In order to "upload" their paper to the blockchain, they will first 
need to add their file/directory to the ipfs distributed file system. This will 
produce a unique reference number (DOI is currently used in journals) 
and hash corresponding to the current paper file/directory. 

The author can then use their address on the Etherum network to create a new contract 
to submit the paper using this reference number and paperID. In this way, there will 
be one paper per contract. The only other action the 
author can make to that paper is submitting another draft. 

Others can review and comment on papers, but an address can not comment/review
its own paper. The reviews are rated on a "work needed", "acceptable" basis 
and the reviewer can also upload an ipfs hash of their comments file/directory. 
Protection is also built in such that others can not submit revisions of the 
original author's paper. 

The blockchain will have a record of the initial paper submitted, revisions made 
by the author, and comments/reviews made by peers. The beauty of all of this is
one can see the full transaction histories and reconstruct the full evolution of 
the document. One can see the initial draft, all suggestions from reviewers, 
how many reviewers, and how many of them think the final draft is reasonable. 

## How we built it
There are 2 main back-end components, the ipfs file hosting service 
and the ethereum blockchain contracts. They are bridged together 
with ([MetaMask](https://metamask.io/)), a tool for connecting 
the distributed blockchain world, and by extension the distributed 
papers, to a web browser. 
 
We wrote a smart contract in the Solidity language used as a high level 
language for writing smart contracts. The ipfs intereface was build using 
DAVID FILL ME IN, INCLUDING DETAILS ABOUT THE WEBPAGE BEING HOSTED ON IPFS
. Then we connected everything using MetaMask and Javascript (BIJAN FILL IN THIS PART)

## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for arXain
