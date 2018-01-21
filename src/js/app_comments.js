App = {
  web3Provider: null,
  contracts: {},

  init: function() {
    return App.initWeb3();
  },

  initWeb3: function() {
    // Is there an injected web3 instance?
    if (typeof web3 !== 'undefined') {
     App.web3Provider = web3.currentProvider;
     console.log('I found a web3 provider');
     } else {
       // If no injected web3 instance is detected, fall back to Ganache
         console.log("I did not find a web3 instance")
         App.web3Provider = new Web3.providers.HttpProvider('http://localhost:8545');
         }
         web3 = new Web3(App.web3Provider);
        return App.initContract();
  },

  initContract: function() {
	$.getJSON('Manuscript.json', function(data) {
	  // Get the necessary contract artifact file and instantiate it with truffle-contract
	  var ManuscriptArtifact = data;
	  App.contracts.Manuscript = TruffleContract(ManuscriptArtifact);

	  // Set the provider for our contract
	  App.contracts.Manuscript.setProvider(App.web3Provider);

	  // do not submit automatically -- catch instead
	  //return App.submitManuscript();
	});

    return App.bindEvents();
  },

  bindEvents: function() {
    $(document).on('click', '.btn-submit', App.handleSubmit);
  },
  handleSubmit: function(event) {
    event.preventDefault();

    var contractAddr = $('.contract_hash').val();
    var commentHash = $('.comment_hash').val();
    console.log('comment hash of type '+typeof(commentHash)+' with val '+commentHash)
    var doi = $('.comment_doi').val();
    console.log('doi of type '+typeof(doi)+' with val '+doi)
    var review = $('input:radio[name=review]:checked').val();
    console.log('review bool of type '+typeof(review)+' with val '+review)
    var manuscriptInstance = App.contracts.Manuscript.at(contractAddr);

	web3.eth.getAccounts(function(error, accounts) {
	  if (error) {
		console.log(error);
	  }

	  var account = accounts[0];
      console.log(typeof(account))
	  manuscriptInstance.reviewManuscript(commentHash, doi, review).then(function(result) {
          $('.results-text').show();
          $('.results-text').text('Successfully submitted comment.');
          console.log('Success');
	    }).catch(function(err) {
		    console.log(err.message);
	    });
    });
  }

};

$(function() {
  $(window).load(function() {
    App.init();
  });
});
