pragma solidity ^0.4.11;

contract arXainBase{
  bytes32[] papers;

  function pushPaper(bytes32 _paperHash) public{
    papers.push(_paperHash);
  }
  
  function getPapers() public constant returns (bytes32[] _papers) {
    return papers;
  }
}
