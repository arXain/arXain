pragma solidity ^0.4.11;

contract Comments{

  bytes32[] comments;
  address contractAddress;
  
  function Comments(address _contractAddress) public{
    contractAddress = _contractAddress;
  }
  
  function commentOnPaper(bytes32 _commentHash) public{
    comments.push(_commentHash);
  }
  
  function getComments() public constant returns (bytes32[] _comments) {
    return comments;
  }
}
