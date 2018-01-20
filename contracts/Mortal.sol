pragma solidity ^0.4.11;

contract Mortal {
    /* Define variable owner of the type address*/
    address owner;

    /* this function is executed at initialization and sets the owner of the contract */
    function Mortal() { 
        owner = tx.origin; 
    }

    function getOwner() constant returns (address) { 
        return owner; 
    }
}
