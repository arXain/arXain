pragma solidity ^0.4.11;

contract Organizations{
  
  struct Member{
    address memberAddress; 
    string memberName;
    uint voteCount; 
  }  

  struct Org {
    address[] papers;
    mapping (address => uint8) votes;
    string orgName;
    Member[] members;
  }

//  function addPaperToOrg( address _paperAddress){
//  }

  //function addMember(address _userAddress) public{
  //  organization.push(_userAddress);
  //}
 
  //function removeMember(address _userAddress) public{
  //  uint toRemove = 99999;
  //  for (uint i = 0; i<organization.length-1; i++){
  //    if(organization[i] == _userAddress)
  //      toRemove = i;
  //  }
  //  if(toRemove != 99999){
  //    delete organization[i];
  //    organization.length--;
  //  }
  //}
  //
  //function orgName() public view return(string){
  //  return org.name
  //}
  //function getMembers() public view returns (address[] _members) {
  //  return organization;
  //}
}
