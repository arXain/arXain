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
    $(document).on('click', '.btn-create', App.handleCreate);
    $(document).on('click', '.btn-submit', App.handleSubmit);
  },

  handleCreate: function(event) {
    event.preventDefault();

    var corpusID = $('#hash-form').find('.submit_hash').val();
    var doi = $('#doi-form').find('.submit_doi').val();

	var manuscriptInstance;

	web3.eth.getAccounts(function(error, accounts) {
	  if (error) {
		console.log(error);
	  }

	  var account = accounts[0];
      console.log('right before manuscript.');
      console.log('account is: '+account);

	  App.contracts.Manuscript.new().then(function(instance) {
        manuscriptInstance = instance;
	  }).catch(function(err) {
        $('.failure-text').show();
		console.log(err.message);
	  });
        $('.success-text').show();
        $('.success-text').text('Put your TX has in the field labeled TX hash.');
		console.log('Successful contract creation.');
        $('.btn-create').hide();
        $('.btn-submit').show();
	});
  },

  handleSubmit: function(event) {
    event.preventDefault();

    var corpusID = $('#hash-form').find('.submit_hash').val();
    var doi = $('#doi-form').find('.submit_doi').val();
    var tx = $('#tx-form').find('.submit_tx').val();
    console.log('trasaction is '+tx);
    //var contractAddr;
    web3.eth.getTransactionReceipt(tx, function(error, result) {
    if(error) {
        console.error(error);
    }
    else {
    var contractAddr = result['contractAddress']; 
    console.log(contractAddr);
    console.log(typeof(contractAddr));

	var manuscriptInstance = App.contracts.Manuscript.at(contractAddr);

	web3.eth.getAccounts(function(error, accounts) {
	  if (error) {
		console.log(error);
	  }

	  var account = accounts[0];

		manuscriptInstance.initialManuscript(corpusID, doi).then(function(result) {
        $('.success-text').text('Success! Here is your contract ID: '+contractAddr);
		console.log('Successful submission');
	  }).catch(function(err) {
        $('.failure-text').show();
		console.log(err.message);
	  });
    });
    };
    });
  }
};

$(function() {
  $(window).load(function() {
    App.init();
  });
});
