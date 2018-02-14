pragma solidity ^0.4.11;

contract Paper{
  Manuscript m;
 
  struct Manuscript {
    address author;
    string paperHash;
    uint8 revision;
    uint8 nInReview;
    uint8 nAccepted;
    address commentAddr;
  }
  
  modifier onlyOwner{
    require(m.author == msg.sender);
    _;
  } 
  
  modifier setOnce{
    require(m.commentAddr == 0x0);
    _;
  } 
  
  function Paper() public{ 
    m = Manuscript(msg.sender, '0x0', 0, 0, 0, 0x0);
  }

  function getPaper() public constant returns (
    address _author, string _paperHash, uint8 _revision,
    uint8 _nInReview, uint8 _nAccepted, address _commentAddr) {
    return(m.author, m.paperHash, m.revision, m.nInReview, m.nAccepted, m.commentAddr);
    }

  function initPaper(string _paperHash) public onlyOwner{
    if (m.revision != 0) return;
    m.paperHash = _paperHash;
    m.revision++;
  }

  function amendPaper(string _paperHash ) public onlyOwner{
    if (m.revision == 0) return;
    /* Most gas efficient was to compare strings */
    // must be revising the on-contract DOI
    // can't just re-upload their old document
    if(keccak256(_paperHash) == keccak256(m.paperHash)) return;
    m.paperHash = _paperHash;
    m.revision++;
  }


  function getPaperHash() public constant returns (string) {
    return m.paperHash;
  }

  function getRevision() public constant returns (uint8){
    return m.revision;
  }

  function getNinReview() public constant returns (uint8){
    return m.nInReview;
  }

  function getNaccepted() public constant returns (uint8){
    return m.nAccepted;
  }

  function review(bool _ans) public{
    if(_ans == true)
      m.nAccepted++;
    else if(_ans == false)
      m.nInReview++;
  }
 
  function setCommentAddr(address _commentAddr) public setOnce{
    m.commentAddr = _commentAddr;
  }

}
