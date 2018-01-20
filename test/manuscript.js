var Manuscript = artifacts.require('./contracts/Manuscript.sol');
contract('Manuscript:getCorpus', function(accounts) {
  it("should return a correct string", function(done) {
    var manuscript = Manuscript.deployed();
    manuscript.then(function(contract){
      return contract.getCorpus.call(); // **IMPORTANT
    }).then(function(result){
      assert.isTrue(result === 'Give me Science!');
      done();
    })
  });
});
