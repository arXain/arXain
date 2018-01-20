pragma solidity ^0.4.11;

contract Manuscript{
    string corpus;
    function Manuscript(){
        corpus = "Give me Science!";
    }
    function getCorpus() constant returns (string) {
        return corpus;
    }
    function setCorpus(string _corpus){
        corpus = _corpus;
    }
}
