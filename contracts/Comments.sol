pragma solidity ^0.4.11;

contract Comments{
  
  //bytes32[] comments;
  string comments;
  address contractAddress;
  uint8 nInReview;
  uint8 nAccepted;
  
  function Comments(address _contractAddress) public{
    contractAddress = _contractAddress;
    nInReview=0;
    nAccepted=0;
  }
  
  function review(string _commentHash, bool _ans) public{
    comments = _commentHash;
    //comments.push(_commentHash);
    if(_ans == true)
      nAccepted++;
    else if(_ans == false)
      nInReview++;
  }

  function getAddress() public constant returns (address _contractAddress) {
    return contractAddress;
  }

  function getComments() public constant returns (string _comments) {
    return comments;
  }

  function getStatus() public constant returns (uint8 _nAccepted, uint8 _nInReview){
    return (nAccepted, nInReview);
  }
 
}
