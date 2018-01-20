var Manuscript = artifacts.require('./contracts/Manuscript.sol');

contract('Manuscript', function(accounts) {
  var manuscript = Manuscript.deployed();
  var corpusID = 'Paper1';
  var corpusID_d2 = 'Paper1_draft2';
  var reviewID = 'review1';
  var reviewID2 = 'review2';
  var doi = '0001';
  var acct1 = accounts[0];
  var acct2 = accounts[1];
  var acct3 = accounts[2];

  it("Who is the original owner", function(done) {
    manuscript.then(function(contract){
      return contract.getAddress.call(); // **IMPORTANT
    }).then(function(result){
      console.log('The original owner address is: ' + result);
      assert.isTrue(result != null);
      done();
    })
  });


 //-----------------------------------------------------------------------------
 // Initialize and  check manuscript
 //-----------------------------------------------------------------------------
 
  it("initialManuscript call", function(done){
    manuscript.then(function(contract){
        return contract.initialManuscript(corpusID,doi, {from: acct1});
    })
    console.log('Call to initialManuscript(corpusID, doi) with:');
    console.log('corpusID = Paper1');
    console.log('doi = 0001');
    done();
  });

  it("Checking after initialManuscript", function(done){
    manuscript.then(function(contract){
        return contract.getManuscript.call();
    }).then(function(results){
      console.log('corpusID:     ' + results[0]);
      console.log('doi:          ' + results[1]);
      console.log('Revision:     ' + results[2]);
      console.log('reviews (nw): ' + results[3]);
      console.log('reviews (A+): ' + results[4]);
      assert.isTrue(results[0] == 'Paper1');
      assert.isTrue(results[1] == '0001');
      assert.isTrue(results[2] == '1');
      assert.isTrue(results[3] == '0');
      assert.isTrue(results[4] == '0'); 
      done();
    });
  });

 //-----------------------------------------------------------------------------
 // Reviewer 1 submits review and check manuscript
 //-----------------------------------------------------------------------------
 
  it("reviewManuscript call", function(done){
    manuscript.then(function(contract){
        return contract.reviewManuscript(reviewID, doi, 0, {from: acct2});
    })
    console.log('from address: ' + acct2);
    console.log('Call to reviewManuscript(reviewID, doi, status) with:');
    console.log('reviewID = review1');
    console.log('doi = 0001');
    console.log('status = 0');
    done();
  });

  it("Checking after reviewManuscript", function(done){
    manuscript.then(function(contract){
        return contract.getManuscript.call();
    }).then(function(results){
      console.log('corpusID:     ' + results[0]);
      console.log('doi:          ' + results[1]);
      console.log('Revision:     ' + results[2]);
      console.log('reviews (nw): ' + results[3]);
      console.log('reviews (A+): ' + results[4]);
      //assert.isTrue(results[0] == 'Paper1');
      //assert.isTrue(results[1] == '0001');
      //assert.isTrue(results[2] == '1');
      //assert.isTrue(results[3] == '0');
      //assert.isTrue(results[4] == '0'); 
      done();
    });
  });

 //-----------------------------------------------------------------------------
 // Submitter amends doc and check manuscript
 //-----------------------------------------------------------------------------
 
  it("amendManuscript call", function(done){
    manuscript.then(function(contract){
        return contract.amendManuscript(corpusID_d2, doi, {from: acct1});
    })
    console.log('from address: ' + acct1);
    console.log('Call to amendManuscript(corpusID, doi) with:');
    console.log('corpusID = Paper1_draft2');
    console.log('doi = 0001');
    done();
  });

  it("Checking after reviewManuscript", function(done){
    manuscript.then(function(contract){
        return contract.getManuscript.call();
    }).then(function(results){
      console.log('corpusID:     ' + results[0]);
      console.log('doi:          ' + results[1]);
      console.log('Revision:     ' + results[2]);
      console.log('reviews (nw): ' + results[3]);
      console.log('reviews (A+): ' + results[4]);
      //assert.isTrue(results[0] == 'Paper1_draft2');
      //assert.isTrue(results[1] == '0001');
      //assert.isTrue(results[2] == '2');
      done();
    });
  });

 //-----------------------------------------------------------------------------
 // Reviewer 2 submits review and check manuscript
 //-----------------------------------------------------------------------------
 
  it("reviewManuscript call", function(done){
    manuscript.then(function(contract){
        return contract.reviewManuscript(reviewID2, doi, 1, {from: acct3});
    })
    console.log('Call to reviewManuscript(reviewID, doi, status) with:');
    console.log('reviewID = review2');
    console.log('doi = 0001');
    console.log('status = 1');
    done();
  });

  it("Checking after reviewManuscript", function(done){
    manuscript.then(function(contract){
        return contract.getManuscript.call();
    }).then(function(results){
      console.log('corpusID:     ' + results[0]);
      console.log('doi:          ' + results[1]);
      console.log('Revision:     ' + results[2]);
      console.log('reviews (nw): ' + results[3]);
      console.log('reviews (A+): ' + results[4]);
      done();
    });
  });

  it("Who is interacting with contract now", function(done) {
    manuscript.then(function(contract){
      return contract.getSender.call({from: acct3}); // **IMPORTANT
    }).then(function(result){
      console.log('The sender address is:         ' + result);
      assert.isTrue(result != null);
      done();
    })
  });

});

