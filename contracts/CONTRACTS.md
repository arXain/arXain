Contract Structure
------

#### arXainBase

TODO: FIX byte32 string issue 


This contract will be depolyed on the blockchain and will just be the index for 
all papers. It has two functions: 

`pushPaper (byte32 _paper)` 
- Adds paper hash to arXain

`getPapers() returns bytes[]` - Get array of paper hashes from arXain


#### Paper

This contract is *the* paper. It's functions are:

`getPaper() returns address _author, string _paperHash,`  
`int8 _revision, address _commentAddr` 
`uint8 _nAccepted, uint8 _nInReview`- This returns info about the paper! Returns the
first author, paper IPFS has, revision number, comment contract address, and number of 
accepted and in review flags.  

`initPaper(string _paperHash)` - Initializes the paper with the first IPFS 
paper hash. This function is only allowed by the author who instantiated the 
contract or an address designated by the author.

`amendPaper(string _paperHash)` - Changes the paper hash of the Paper. 
The paper hash must be different from the previous hash. 
This function is only allowed by the author who instantiated the contract or an i
address designated by the author.

`setCommentAddr(address _commentAddr)` - To be used by an author to set address of the comment contract.
This can only be set once.   


#### Comments

`review(bytes32 _commentHash, bool _ans)` - Review the paper. Adds comment 
hash from IPFS and a boolean (radio button) for need's work / acceptable flag.

`getComments()  returns bytes32[] _comments` - Get array of comment hashes for the paper.

`getStatus() returns uint8 _nAccepted, uint8 _nInReview` - Returns the status flags.

#### Organizations

TODO better 
