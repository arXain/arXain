pragma solidity ^0.4.11;

contract arXainBase{
  address[] papers;

  function addPaper(address _paperHash) public{
    papers.push(_paperHash);
  }
  
  function getPapers() view public returns (address[] _papers) {
    return papers;
  }
}
