pragma solidity ^0.4.11;

contract Paper{
   
  address[] private authors;
  mapping (address => uint) public authorsMap;
  string private paperHash;
  int8 private revision = -1;
  address private commentAddr;

  modifier onlyAuthors {
    require(authorsMap[msg.sender] != 0);
    _;
  }
  
  function addAuthor(address newAuthor) onlyAuthors public {
    uint id = authorsMap[newAuthor];
    if (id == 0) {
      authorsMap[newAuthor] = (authors.length + 1);
    }
  }
 
  modifier setOnce{
    require(commentAddr == 0x0);
    _;
  } 
 
   modifier constructOnce{
    require(revision == 0);
    _;
  } 
 
  function Paper() public { 
    paperHash = '0x1'; 
    revision = 0;
    commentAddr = 0x0;
    authors.push(msg.sender);
    authorsMap[msg.sender] = 1;
  }

  function getPaper() view public returns (address[],string,int8,address) {
    return(authors, paperHash, revision, commentAddr);
    }

  function initPaper(string _paperHash, address _commentAddr) public onlyAuthors constructOnce{
    paperHash = _paperHash;
    commentAddr = _commentAddr; 
    revision++;
  }

  function amendPaper(string _paperHash ) public onlyAuthors{
    if(revision == 0) return;
    // can't just re-upload their old document
    if(keccak256(_paperHash) == keccak256(paperHash)) return;
    paperHash = _paperHash;
    revision++;
  }

}

