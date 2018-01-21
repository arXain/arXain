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
    $(document).on('click', '.btn-check', App.handleSubmit);
  },
  handleSubmit: function(event) {
    event.preventDefault();

    var contractAddr = $('.status_hash').val();
    var manuscriptInstance = App.contracts.Manuscript.at(contractAddr);
    console.log('contract address: '+contractAddr);

	web3.eth.getAccounts(function(error, accounts) {
	  if (error) {
		console.log(error);
	  }

	  var account = accounts[0];
      console.log(typeof(account))
	  manuscriptInstance.getManuscript().then(function(result) {
          $('.results-text').show();
          $('.results-text').html(
          '<b>paperID:</b> '+result[0]+'<br>'+
          '<b>doi:</b> '+result[1]+'<br>'+
          '<b>revision #:</b> '+result[2]+'<br>'+
          '<b>reviews (Needs work):</b> '+result[3]+'<br>'+
          '<b>reviews (Acceptable):</b> '+result[4]+'<br>'+
          '<b>IPFS link:</b> <a href="http://localhost:8080/ipfs/'+result[0]+'">http://localhost:8081/ipfs/'+result[0]+'</a><br>'
          );
          console.log(
          'paperID: '+result[0]+'\n'+
          'doi: '+result[1]+'\n'+
          'revision #: '+result[2]+'\n'+
          'reviews (needs work): '+result[3]+'\n'+
          'reviews (Acceptable): '+result[4]+'\n'
          );
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
