pragma solidity ^0.4.11;

import "./Mortal.sol";

contract Manuscript{
    Mortal author;
    string corpusID;
    string doi;
    uint8 revision;
    string[] reviewIDs;
    uint8 nInReview;
    uint8 nAccepted;

    function Manuscript(){
        author = new Mortal();
        corpusID = '0x0';
        doi = '0x0';
        revision = 0;
        nInReview = 0;
        nAccepted = 0;
    }

    function getManuscript() constant returns (
        string _corpusID, string _doi, uint8 _revision,
        uint8 _nInReview, uint8 _nAccepted) {
            return(corpusID, doi, revision, nInReview, nAccepted);
        }

    function initialManuscript(string _corpusID, string _doi){
        /*
        TODO: PATCH TRUFFLE FUNCTIONALITY
        if (msg.sender != getAddress()) return;
        */
        if (revision != 0) return;
        setCorpusID(_corpusID);
        setDoi(_doi);
        revision++;
    }

    function reviseManuscript(string _corpusID, string _doi){
        /*
        TODO: PATCH TRUFFLE FUNCTIONALITY
        if (msg.sender != getAddress()) return;
        */
        if (revision == 0) return;
        /* Most gas efficient was to compare strings */
        // must be revising the on-contract DOI
        if(keccak256(_doi) != keccak256(doi)) return;
        // can't just re-upload their old document
        if(keccak256(_corpusID) == keccak256(corpusID)) return;

        setCorpusID(_corpusID);
        revision++;
    }

    function reviewManuscript(string _reviewID, string _doi,
                              uint8 _status){
        /*
        TODO: PATCH TRUFFLE FUNCTIONALITY
        // can't be reviewed by owner
        if (msg.sender == getAddress()) return;
        */

        // must be reviewing the on-contract DOI
        if(keccak256(_doi) != keccak256(doi)) return;
        /*
            valid review statuses:
                0 => "needs improvement"
                1 => "good to go"
        */
        if (_status == 0){
            nInReview++;
            reviewIDs.push(_reviewID);
        }
        else if (_status == 1){
            nAccepted++;
        }
        else return;
    }

    function getNinReview() constant returns (uint8){
        return nInReview;
    }

    function getNaccepted() constant returns (uint8){
        return nAccepted;
    }

    function getNreviews() constant returns (uint8){
        return uint8(reviewIDs.length);
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
