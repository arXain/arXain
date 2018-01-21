App = {
  web3Provider: null,
  contracts: {},

  init: function() {
    // Load paper.
    $.getJSON('../papers.json', function(data) {
      var articleRow = $('#articleRow');
      var articleTemplate = $('#articleTemplate');

      for (i = 0; i < data.length; i ++) {
        articleTemplate.find('.article-title').text(data[i].title);
        articleTemplate.find('.article-title').attr('href', "http://localhost:8080/ipns/"+data[i].submitter+"/"+data[i].doi+"/"+data[i].doi+".pdf")
        articleTemplate.find('.article-authors').text(data[i].authors);
        articleTemplate.find('.article-submitter').text(data[i].submitter);
        articleTemplate.find('.article-tags').text(data[i].tags);
        articleTemplate.find('.article-doi').text(data[i].doi);
        articleTemplate.find('.article-abstract').text(data[i].abstract);
        articleTemplate.find('.article-date').text(data[i].timestamp);

        articleRow.append(articleTemplate.html());
      }
    });

    //return App.initWeb3();
  },
  /*
  initWeb3: function() {
    // Is there an injected web3 instance?
    if (typeof web3 !== 'undefined') {
     App.web3Provider = web3.currentProvider;
     } else {
       // If no injected web3 instance is detected, fall back to Ganache
         App.web3Provider = new Web3.providers.HttpProvider('http://localhost:8545');
         }
         web3 = new Web3(App.web3Provider);

    return App.initContract();
  },

  initContract: function() {
    $.getJSON('Adoption.json', function(data) {
      // Get the necessary contract artifact file and instantiate it with truffle-contract
      var AdoptionArtifact = data;
      App.contracts.Adoption = TruffleContract(AdoptionArtifact);

      // Set the provider for our contract- again this should be MetaMask
      App.contracts.Adoption.setProvider(App.web3Provider);

      // Use our contract to retrieve and mark the adopted pets
      return App.markAdopted();
    });

    return App.bindEvents();
  },

  bindEvents: function() {
    $(document).on('click', '.btn-adopt', App.handleAdopt);
  },

  markAdopted: function(adopters, account) {
  },

  handleAdopt: function(event) {
    event.preventDefault();

    var petId = parseInt($(event.target).data('id'));

  }
  */
};

$(function() {
  $(window).load(function() {
    App.init();
  });
});
