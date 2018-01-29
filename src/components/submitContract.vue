<!-- Navbar Component -->
<template>
<div class="panel panel-default panel-article">
  <div class="panel-heading">
	  <h3 class="panel-title"><center>Submit here</center></h3>
  </div>
  <div class="panel-body">
	<center>
	<div class="form-group" id="hash-form">
	  <strong>Paper Hash</strong>: <input type="text" placeholder="Paper Hash" class="submit_hash">
	</div>
	<div class="form-group" id="doi-form">
	  <strong>DOI</strong>: <input type="text" placeholder="DOI" class="submit_doi">
	</div>
	<div class="form-group" id="tx-form">
	  <strong>TX Address</strong>: <input type="text" placeholder="Leave empty for now" class="submit_tx">
	</div>
	<button type="submit" class="btn btn-default btn-create">Create Contract</button>
	<button type="submit"  class="btn btn-default btn-submit">Submit Paper</button>
	<br><br>
	<span style="display: none;" class="success-text">Success!</span><br>
	<span style="display: none;" class="failure-text">Failed to submit paper!</span><br>
	</center>
  </div>
</div>
</div>
</template>

<script>
appSubmit = {
  web3Provider: null,
  contracts: {},

  init: function() {
    return appSubmit.initWeb3();
  },

  initWeb3: function() {
    // Is there an injected web3 instance?
    if (typeof web3 !== 'undefined') {
     appSubmit.web3Provider = web3.currentProvider;
     console.log('I found a web3 provider');
     } else {
       // If no injected web3 instance is detected, fall back to Ganache
         console.log("I did not find a web3 instance")
         appSubmit.web3Provider = new Web3.providers.HttpProvider('http://localhost:8545');
         }
         web3 = new Web3(appSubmit.web3Provider);
        return appSubmit.initContract();
  },

  initContract: function() {
	$.getJSON('build/contracts/Manuscript.json', function(data) {
	  // Get the necessary contract artifact file and instantiate it with truffle-contract
	  var ManuscriptArtifact = data;
	  appSubmit.contracts.Manuscript = TruffleContract(ManuscriptArtifact);

	  // Set the provider for our contract
	  appSubmit.contracts.Manuscript.setProvider(appSubmit.web3Provider);

	  // do not submit automatically -- catch instead
	  //return appSubmit.submitManuscript();
	});

    return appSubmit.bindEvents();
  },

  bindEvents: function() {
    $(document).on('click', '.btn-create', appSubmit.handleCreate);
    $(document).on('click', '.btn-submit', appSubmit.handleSubmit);
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

	  appSubmit.contracts.Manuscript.new().then(function(instance) {
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

	var manuscriptInstance = appSubmit.contracts.Manuscript.at(contractAddr);

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

module.exports = {
	data(){
        appSubmit.init(); 
	}
};
</script>


<style scoped>

</style>
