## Inspiration
Peer-review science is critical to modern science, engineering, and healthcare endeavors. 
However, the system for implementing this process has lagged behind and results 
in expensive costs for publishing and accessing material, long turn around times 
reminiscent of snail-mail, and shockingly opaque editorial practices. Astronomy, 
Physics, Mathematics, and Engineering using a "pre-print server" ([arXiv](https://arxiv.org)) 
which was the early internets improvement upon snail-mailing articles 
to researchers around the world. This pre-print server is maintained 
by a single University, and is constantly requesting donations to keep up the 
servers and maintenance. While researchers widely acknowledge the importance of 
the pre-print server, there is no peer-review incorporated, and none planned 
due to technical reasons. Thus, researchers are stuck with spending >$1000 per 
paper to be published in Journals, all the while individual article access 
can cost as high as $32 per paper! 
([source](https://www.nature.com/subscriptions/purchasing.html)). For reference, 
a single PhD thesis can contain >150 references, or essentially cost $4800 if purchased individually.

The recent advance of blockchain and smart contract technology 
([Ethereum](https://www.ethereum.org/)) coupled with decentralized 
file sharing networks ([InterPlanetaryFileSystem](https://ipfs.io)) 
naturally lead us to believe that archaic journals and editors could 
be bypassed. We fashioned our manuscript distribution and reviewing 
platform based on the arXiv, but in a completely decentralized manner. 
Users utilize, maintain, and grow the network of scholarship by simply running a simple program and web interface.

(https://github.com/david-hopper/arXain/blob/master/src/images/logo_small.png?raw=true)

## What it does

## How we built it
There are 2 main back-end components, the ipfs file hosting service 
and the ethereum blockchain contracts. They are bridged togeher 
with ([MetaMask](https://metamask.io/)), a tool for connecting 
the distributed blockchain world, and by extension the distributed 
papers, to a web browser. 
 
We wrote a smart contract that deals with all the apects of a peer-reviewed 
journal. An address on the Etherum network can submit paper, review and 
comment on other papers, revise their own submitted papers, 

## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for arXain
