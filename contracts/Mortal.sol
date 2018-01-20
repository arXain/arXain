contract Mortal {
    /* Define variable owner of the type address*/
    address owner;

    /* this function is executed at initialization and sets the owner of the contract */
    function Mortal() { 
        owner = msg.sender; 
    }

    function getOwner() constant returns (address) { 
        return owner; 
    }
}
