var Manuscript = artifacts.require('./contracts/Manuscript.sol');
contract('Manuscript:getAddress', function(accounts) {
  it("should return an address", function(done) {
    var manuscript = Manuscript.deployed();
    manuscript.then(function(contract){
      return contract.getAddress.call(); // **IMPORTANT
    }).then(function(result){
      assert.isTrue(result != null);
      console.log(result);
      done();
    })
  });
});
contract('Manuscript:getSender', function(accounts) {
  it("should return an senderAddress", function(done) {
    var manuscript = Manuscript.deployed();
    manuscript.then(function(contract){
      return contract.getSender.call(); // **IMPORTANT
    }).then(function(result){
      assert.isTrue(result != null);
      console.log(result);
      done();
    })
  });
});
