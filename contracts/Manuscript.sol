pragma solidity ^0.4.11;

import "./Mortal.sol";

contract Manuscript{
    Mortal author;
    string corpusID;
    string doi;
    uint8 revision;

    enum reviewStatus {unreviewed, needsWork, accepted}
    reviewStatus status;

    function Manuscript(){
        author = new Mortal();
        corpusID = '0x0';
        doi = '0x0';
        revision = 0;
        status = reviewStatus.unreviewed;
    }

    function initialManuscript(string _corpusID, string _doi){
        /*
        TODO: PATCH TRUFFLE FUNCTIONALITY
        if (msg.sender != getAddress()) return;
        */
        if (revision != 0) return;
        setCorpusID(_corpusID);
        setDoi(_doi);
    }

    function reviseManuscript(string _corpusID, string _doi){
        /*
        TODO: PATCH TRUFFLE FUNCTIONALITY
        if (msg.sender != getAddress()) return;
        */
        if (revision == 0) return;
        if(keccak256(_doi) != keccak256(doi)) return;
        setCorpusID(_corpusID);
        revision++;
    }


    function getStatus() constant returns (uint){
        return uint(status);
    }

    function setStatus(reviewStatus _status){
        status = _status;
    }

    function getRevision() constant returns (uint8){
        return revision;
    }

    function getCorpusID() constant returns (string) {
        return corpusID;
    }

    function setCorpusID(string _corpusID){
        corpusID = _corpusID;
    }

    function getDoi() constant returns (string){
        return doi;
    }

    function setDoi(string _doi){
        doi = _doi;
    }

    function getAddress() constant returns (address) {
        return author.getOwner();
    }
    //testing
    function getSender() constant returns (address) {
        return msg.sender;
    }
}
