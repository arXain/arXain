var Manuscript = artifacts.require('./contracts/Manuscript.sol');

contract('Manuscript', function(accounts) {
  var manuscriptInstance;
  var corpusID = 'myCorpusHash'
  var doi = 'myDOI'

  it("should return default manuscript attributes", function() {
    Manuscript.deployed().then(function(instance){
      return contract.getManuscript.call(); // **IMPORTANT
    }).then(function(data){
        assert.equal(data[0], '0x0','corpusID must be empty');
        assert.equal(data[1], '0x0','DOI must be empty');
        assert.equal(data[2], 0, 'revision must be zero');
        assert.equal(data[3], 0, 'no reviews (needs work)');
        assert.equal(data[4], 0, 'no reviews (good)');
    });
  });

  it("should change corpusID, DOI, revision", function(){
      Manuscript.deployed().then(function(instance){
        return contract.initialManuscript(corpusID,doi);
  }).then(function(instance){
      assert.equal(instance.getCorpusID(),'myCorpusHash','hash should change');
      assert.equal(instance.getDoi(),'myDOI','DOI should change');
      assert.equal(instance.getRevision(),1,'revision should advance')
  });
});



});


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
