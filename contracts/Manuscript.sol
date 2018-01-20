pragma solidity ^0.4.11;

import "./Mortal.sol";

contract Manuscript{
    string corpus;
    Mortal m;

    function Manuscript(){
        corpus = "Give me Science!";
        m = new Mortal();
    }
    
    function getCorpus() constant returns (string) {
        return corpus;
    }
    
    function setCorpus(string _corpus){
        corpus = _corpus;
    }
    
    function getAddress() constant returns (address) {
        return m.getOwner();
    }
}
