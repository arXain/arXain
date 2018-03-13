Contract Structure
------

#### arXainBase

This contract will be depolyed on the blockchain and will just be the index for 
all papers. It has two functions: 

`pushPaper (address)` 
- Adds paper hash to arXain

`getPapers() returns address[]` - Get array of paper hashes from arXain


#### Paper

This contract is *the* paper. It's functions are:

`getPaper() returns address,string,int8, address` - This returns info about the paper! Returns the
first author, paper IPFS has, revision number, comment contract address, and number of 
accepted and in review flags.  

`initPaper(string)` - Initializes the paper with the first IPFS 
paper hash. This function is only allowed by the author who instantiated the 
contract or an address designated by the author.

`amendPaper(string)` - Changes the paper hash of the Paper. 
The paper hash must be different from the previous hash. 
This function is only allowed by the author who instantiated the contract or an 
address designated by the author.

`setCommentAddr(address)` - To be used by an author to set address of the comment contract.
This can only be set once.   


#### Comments
`Comments(address)` - Initializes comment contract and sets paper contract address for 
reference

`review(string, uint8)` - Review the paper. Adds comment 
hash from IPFS and a paper status (options) for need's work / acceptable flag.

`getPaperAddress() return address` - Get address of paper contract.

`getStatus() returns uint8, uint8` - Gets the status flags.

`getComment(address) returns string, uint8` - Gets the commentHash and status bit for commenter address.

`getReviewers() returns address[]` - Gets array of all commentor addresses.

`getCommentsLength() returns uint` - Get number of comments/commentors.

#### Organizations

TODO better 
