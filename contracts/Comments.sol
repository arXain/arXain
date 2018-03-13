pragma solidity ^0.4.11;

contract Comments{
  
  address contractAddress;
  
  struct Reviewer {
    string commentHash;
    uint8 status;
  }
 
  mapping(address => Reviewer) reviewers;
  address[] reviewerAccounts;
  
  function Comments(address _contractAddress) public{
    contractAddress = _contractAddress;
  }
  
  function review(string _commentHash, uint8 _status) public{
    
    var reviewer=reviewers[msg.sender];
    reviewer.commentHash = _commentHash;
    reviewer.status = _status;
    
    reviewerAccounts.push(msg.sender) -1;

  }

  function getPaperAddress() view public returns (address) {
    return contractAddress;
  }

  function getComment(address _address) view public returns (string,uint8) {
    return (reviewers[_address].commentHash, reviewers[_address].status);
  }

  function getReviewers() view public returns (address[]) {
    return reviewerAccounts;
  }
  
  function getCommentsLength() view public returns (uint) {
        return reviewerAccounts.length;
  }

  function getStatus() view public returns (uint8,uint8){
    uint8 nAccepted = 0; uint8 nInReview = 0;
    for (uint i = 0; i < reviewerAccounts.length; i++) {
      if(reviewers[reviewerAccounts[i]].status == 0)
        nInReview++;
      else if(reviewers[reviewerAccounts[i]].status == 0)
        nAccepted++;
    }
    return (nAccepted, nInReview);
  }
 
}
