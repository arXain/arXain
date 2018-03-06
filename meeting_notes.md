------
**3/5/2018**

Recap:

- Khilesh demoed his mongodb example of scraping the arXiv, and him and Saul tested searching which appears to be very fast. Looks like we can move forwards with that for our backend! Merged in the clean-pyXain and meta-data branches from David and Bijan for handling edge cases cases.

- Saul: Mongodb will be kept on our server and keep track all meta data posted to the arXain (our service)

- How to keep track of other nodes submitting through pub-sub or some other messaging protocol? Submit the contract address and directory hash (and version?) so we can grab the meta data and store it on our server. also watch the block chain.

- Need to look into pub-sub! - David

- Bijan and David: Decided that we need to have a way of removing material posted to IPFS, but for some reason didn’t get published to the blockchain. There must also be another handshake between the final submission and pyXain that locks down a paper from being removed.

- Creating the submit comment page:
  - authors can comment on their own, notifying of a new version and 

  - the submitter of a comment should be stored in the comment contract

  - Can we curate a list of approved individuals, equate ethereum wallet address and identity

  - As contracts increase in size (say a lot of comments are added) it costs more to add to it. prevent trolls

  - Comment contract should not allow the submitting author(s) to vote on whether it is publishable - Khilesh taking this.

  - meta data should contain the following information
	   - list of previous commenters
	   - time of comment
	   - version of paper
	   - comment submitter
	   - vote status

  - comment contract should record who voted accepted or rejected and those people can change their status

To-Do:

Start separating out major projects in the arXain organization
	
 - arXain-node, open source,  David 
	
 - backend searching, propietary, Khilesh and Saul
	
 - website + contracts - open source - Bijan
	
 - meeting notes - open  - David

------
**2/27/2018**

Recap:

 Moved arXain to public arXain/arXain repo and licensed with GNU GPL3. Travis CI integration underway!
 
Notes:
* Bijan and Khilesh working on integrating all contracts on meta-data branch

* Decided on GNU GPL3 license

* Moved to public repo under organization arXain

* David brings up good point about user's running ETH nodes for multi-user tests. Right now we will use testnet on AWS as centralized minichain

* Saul showed intro to Travis CI. Awesome! Travis CI first succesful test! 

To Dos:
* Saul/Khilesh MongoDB investigations this week
* Bijan/Khilesh fix contracts
* David pinning documents/pyXain dev

------
**2/13/2018**

Recap:

Successfully merged the three major feature branches into master (contracts, website, local node).

Notes jotted down during our demo's and discussions

* Store a hash of the submitted paper on the blockchain, to prevent people from duplicating?

* Co-authors as pinners of papers can prevent orphaning of papers on IPFS

* Add co-author addresses who have editing permission to the contract (Don’t add every co-author to prevent bloat of the contract)

* Discussing ideas for pictures for landing pages: "arXain: Distributed Indexing with Distributed Storage"

* Pinning others articles should be fostered, and called "safety pins"

Out standing to-do's:

* Bijan: Incorporate the flask api with submit contract and run an IPFS node on the server

* Khilesh: Contract fixes and connecting them. 

* Khilesh: Image describing arXain

* David: Look over open source documentation, FAQ, assign if things need updating.

* David: incorporate local node pinning and keeping track of pinned items

* Saul: landing page makeover

* All: make a plan for 1517 meeting.

* Transfer to arXain repo and go public


------
**2/6/2018**

Target two weeks for version 0, update 1517 and ask about licensing for this project and any other outstanding issues. 
Primary goal for v0 is to be able to submit multiple manuscripts on a locally running testnet.

v0 checklist:
* Website UI - Bijan/Saul
* Contract - Khilesh/Saul
* flask node - David/Saul

Other to-do:
* Sign up for AWS credit: Saul
* Transfering repository to github.com/arXain

Next meeting goal:
Start connecting Website with contracts and website with local node

------
